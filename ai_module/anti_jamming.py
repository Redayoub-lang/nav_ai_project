import numpy as np
from sklearn.ensemble import IsolationForest
from visualizer import plot_flight_telemetry

def run_ai_protection():
    print("=========================================")
    print("[AI Module] Initializing Anti-Jamming Subsystem...")
    print("=========================================\n")

    # 1. توليد بيانات نظيفة لتدريب النموذج (Baseline Data)
    np.random.seed(42)
    clean_data = np.random.normal(loc=[0, 0, 10, 35], scale=[0.1, 0.1, 0.2, 2.0], size=(100, 4))
    
    model = IsolationForest(contamination=0.15, random_state=42)
    model.fit(clean_data)
    print("[AI Module] IsolationForest Trained on Clean Telemetry.")

    # 2. محاكاة قراءات الحساسات والارتفاع 3D مع هجمات تشويش
    time_steps = list(range(20))
    telemetry_data = []
    anomalies = []

    for t in time_steps:
        # مسار طيران مع ارتفاع تدريجي
        pos_x = t * 0.5
        pos_y = np.sin(t * 0.3) * 2.0
        pos_z = 0.5 * t
        
        # محاكاة هجوم تشويش عند الخطوات t=6, 7, 14
        if t in [6, 7, 14]:
            gps_snr = np.random.uniform(2.0, 8.0) # هبوط حاد في الإشارة (Jamming)
        else:
            gps_snr = np.random.uniform(30.0, 40.0) # إشارة سليمة

        data_sample = [pos_x, pos_y, pos_z, gps_snr]
        telemetry_dict = {'x': pos_x, 'y': pos_y, 'z': pos_z, 'gps_snr': gps_snr}
        telemetry_data.append(telemetry_dict)

        # التنبؤ بواسطة AI
        prediction = model.predict([data_sample])[0]
        is_jammed = (prediction == -1) or (gps_snr < 15.0)
        anomalies.append(is_jammed)

        status = "🔴 JAMMING DETECTED! Switching to Vision/IMU" if is_jammed else "🟢 GPS Signal Normal"
        print(f"T+{t}s | Pos: ({pos_x:.1f}, {pos_y:.1f}, {pos_z:.1f}) | SNR: {gps_snr:.1f} dB -> {status}")

    # 3. عرض واستخراج الرسم البياني
    plot_flight_telemetry(time_steps, telemetry_data, anomalies)

if __name__ == "__main__":
    run_ai_protection()