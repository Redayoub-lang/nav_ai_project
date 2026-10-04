import numpy as np

class AntiJammingFilter:
    def __init__(self, snr_threshold=15.0):
        self.snr_threshold = snr_threshold
        self.last_valid_pos = None
        self.corrected_trajectory = []

    def process_step(self, telemetry_state, snr_level, dt=0.1):
        """
        telemetry_state : [x, y, z, vx, vy, vz, roll, pitch, yaw, wx, wy, wz]
        """
        raw_pos = np.array(telemetry_state[0:3])
        velocity = np.array(telemetry_state[3:6])
        
        is_jammed = snr_level < self.snr_threshold
        
        if not is_jammed:
            # Mode Nominal : Recalage GPS
            corrected_pos = raw_pos
            self.last_valid_pos = corrected_pos.copy()
        else:
            # Mode Anti-Brouillage : Intégration Inertielle (Dead Reckoning)
            if self.last_valid_pos is not None:
                corrected_pos = self.last_valid_pos + velocity * dt
                self.last_valid_pos = corrected_pos.copy()
            else:
                corrected_pos = raw_pos
                
        self.corrected_trajectory.append(corrected_pos)
        return corrected_pos, is_jammed