import numpy as np

class EKFNavFilter:
    """
    Filtre de Kalman Étendu (EKF) pour la navigation sous brouillage GPS.
    État x = [x, y, z, vx, vy, vz]^T
    """
    def __init__(self, dt=0.1, snr_threshold=15.0):
        self.dt = dt
        self.snr_threshold = snr_threshold
        
        # Vecteur d'état initial [x, y, z, vx, vy, vz]
        self.x = np.zeros((6, 1))
        
        # Matrice de covariance d'état initiale
        self.P = np.eye(6) * 0.1
        
        # Matrice de transition d'état F
        self.F = np.eye(6)
        self.F[0, 3] = dt
        self.F[1, 4] = dt
        self.F[2, 5] = dt
        
        # Matrice d'observation H (mesure directe de la position [x, y, z])
        self.H = np.zeros((3, 6))
        self.H[0, 0] = 1.0
        self.H[1, 1] = 1.0
        self.H[2, 2] = 1.0
        
        # Bruit de processus (Q) et Bruit de mesure GPS (R)
        self.Q = np.eye(6) * 0.05
        self.R = np.eye(3) * 0.5

    def predict(self, acceleration=np.zeros(3)):
        """Étape de prédiction (Modèle cinématique 3D)"""
        # Prédiction d'état
        self.x = self.F @ self.x
        self.x[3:6, 0] += acceleration * self.dt
        
        # Prédiction de la covariance
        self.P = self.F @ self.P @ self.F.T + self.Q
        return self.x[:3, 0]

    def update(self, gps_measurement):
        """Étape de mise à jour si le GPS est valide"""
        z = np.array(gps_measurement).reshape(3, 1)
        y = z - (self.H @ self.x)  # Innovation (erreur de mesure)
        S = self.H @ self.P @ self.H.T + self.R  # Covariance de l'innovation
        K = self.P @ self.H.T @ np.linalg.inv(S)  # Gain de Kalman
        
        self.x = self.x + (K @ y)
        self.P = (np.eye(6) - K @ self.H) @ self.P
        return self.x[:3, 0]

    def process_step(self, raw_pos, velocity, snr_level):
        """Gestion dynamique selon la qualité du signal GPS"""
        self.x[3:6, 0] = velocity  # Mise à jour des vitesses
        self.predict()
        
        is_jammed = snr_level < self.snr_threshold
        
        if not is_jammed:
            # Signal GPS correct : Recalage par Kalman
            estimated_pos = self.update(raw_pos)
        else:
            # Brouillage détecté : Conservation de la prédiction EKF
            estimated_pos = self.x[:3, 0]
            
        return estimated_pos, is_jammed