import numpy as np
import csv
from ai_module.anti_jamming import AntiJammingFilter
from ai_module.ekf_filter import EKFNavFilter

def run_performance_benchmark(csv_path="flight_telemetry_report.csv"):
    """
    Compare l'erreur de position (RMSE) entre le Dead Reckoning (INS) 
    et le Filtre de Kalman Étendu (EKF) lors des attaques par brouillage GPS.
    """
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except Exception as e:
        print(f"[!] Erreur de chargement des données : {e}")
        return

    dr_filter = AntiJammingFilter(snr_threshold=15.0)
    ekf_filter = EKFNavFilter(dt=0.1, snr_threshold=15.0)

    dr_errors = []
    ekf_errors = []
    jammed_count = 0

    for step, row in enumerate(data):
        snr = float(row.get('GPS_SNR_dB', 20.0))
        # Trajectoire théorique de référence (Ground Truth)
        true_pos = np.array([float(row.get('Raw_X', 0)), float(row.get('Raw_Y', 0)), float(row.get('Raw_Z', 0))])
        
        # Simulation d'un bruit GPS hors zone de brouillage
        noise = np.random.normal(0, 0.2, 3) if snr >= 15.0 else np.random.normal(2.0, 5.0, 3)
        gps_measured = true_pos + noise
        velocity = np.array([0.5, 0.1, 0.2])

        # Exécution des deux filtres
        dr_pos, is_jammed = dr_filter.process_step(list(gps_measured) + list(velocity) + [0]*6, snr)
        ekf_pos, _ = ekf_filter.process_step(gps_measured, velocity, snr)

        if is_jammed:
            jammed_count += 1
            dr_errors.append(np.linalg.norm(dr_pos - true_pos))
            ekf_errors.append(np.linalg.norm(ekf_pos - true_pos))

    # Calcul des erreurs quadratiques moyennes (RMSE)
    dr_rmse = np.sqrt(np.mean(np.square(dr_errors))) if dr_errors else 0.0
    ekf_rmse = np.sqrt(np.mean(np.square(ekf_errors))) if ekf_errors else 0.0

    print("=================================================================")
    print("      BENCHMARK DE PERFORMANCE NAVIGATION ANTI-BROUILLAGE        ")
    print("=================================================================")
    print(f"• Échantillons analysés sous brouillage (SNR < 15 dB) : {jammed_count}")
    print("-----------------------------------------------------------------")
    print("Méthode d'Estimation           | Erreur Moyenne (RMSE) | Réduction d'Erreur")
    print("-------------------------------+-----------------------+------------------")
    print(f"Dead Reckoning (INS Pur)       | {dr_rmse:.4f} m          | Référence")
    reduction = ((dr_rmse - ekf_rmse) / dr_rmse * 100) if dr_rmse > 0 else 0.0
    print(f"Filtre de Kalman Étendu (EKF)  | {ekf_rmse:.4f} m          | -{reduction:.2f} %")
    print("=================================================================\n")

if __name__ == "__main__":
    run_performance_benchmark()