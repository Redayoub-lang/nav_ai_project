import numpy as np
from sklearn.ensemble import IsolationForest
import time

class AINavSecurity:
    def __init__(self):
        print("=========================================")
        print("[AI Module] Initializing Anti-Jamming Subsystem...")
        print("=========================================\n")
        # إعداد النموذج: نفترض أن 5% من البيانات قد تكون محاولات اختراق أو تشويش
        self.model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        self.is_trained = False

    def train_baseline(self, clean_sensor_data):
        print("[AI Module] Training model on clean GPS/IMU flight data (Baseline)...")
        self.model.fit(clean_sensor_data)
        self.is_trained = True
        print("[AI Module] Training complete. Threat detection is ARMED.\n")

    def analyze_telemetry(self, live_sensor_data):
        if not self.is_trained:
            raise RuntimeError("Cannot analyze telemetry. Model is not trained.")
        
        # التنبؤ: القيمة 1 تعني بيانات آمنة، -1 تعني اكتشاف هجوم أو تشويش
        predictions = self.model.predict(live_sensor_data)
        return predictions

if __name__ == "__main__":
    ai_security = AINavSecurity()
    
    # 1. تدريب النظام على بيانات طيران آمنة ومستقرة (أشبه بالوضع الطبيعي للطائرة)
    # توليد 500 قراءة لـ 12 متغير (تطابق أبعاد الحالة x في C++)
    clean_flight_data = np.random.normal(loc=0.0, scale=1.0, size=(500, 12))
    ai_security.train_baseline(clean_flight_data)
    
    # 2. محاكاة رحلة حية تتعرض لهجوم تشويش
    print("[AI Module] Monitoring live flight telemetry...\n")
    time.sleep(1)
    
    # 5 قراءات طبيعية، تليها قراءة واحدة شاذة جداً (محاكاة فقدان أو تشويش إشارة الـ GPS)
    live_data = np.random.normal(loc=0.0, scale=1.0, size=(6, 12))
    live_data[5] = live_data[5] * 20.0 # تضخيم القيم لتمثيل نبضة التشويش
    
    analysis_results = ai_security.analyze_telemetry(live_data)
    
    for i, status in enumerate(analysis_results):
        if status == 1:
            print(f"T+{i}ms: 🟢 Signals Secure. Navigating normally.")
        else:
            print(f"T+{i}ms: 🔴 JAMMING DETECTED! Blocking GPS. Switching to Vision/IMU.")
            
    print("\n[AI Module] Simulation finished.")