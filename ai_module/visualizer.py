import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_flight_telemetry(time_steps, telemetry_data, anomalies):
    """
    يقوم برسم مسار الطائرة 3D والرسومات البيانية للإشارات مع تمييز نقاط التشويش
    """
    fig = plt.figure(figsize=(14, 6))
    
    # 1. الرسم البياني ثلاثي الأبعاد 3D Plot
    ax1 = fig.add_subplot(121, projection='3d')
    x = [data['x'] for data in telemetry_data]
    y = [data['y'] for data in telemetry_data]
    z = [data['z'] for data in telemetry_data]
    
    ax1.plot(x, y, z, label='UAV Flight Path', color='b', linewidth=2)
    
    # تمييز نقاط التشويش بالأحمر
    for i, is_anomaly in enumerate(anomalies):
        if is_anomaly:
            ax1.scatter(x[i], y[i], z[i], color='red', s=60, marker='o', label='Jamming Detected' if i == anomalies.index(True) else "")

    ax1.set_title('3D UAV Navigation Path & Anti-Jamming Events')
    ax1.set_xlabel('X (m)')
    ax1.set_ylabel('Y (m)')
    ax1.set_zlabel('Altitude Z (m)')
    ax1.legend()

    # 2. رسم الإشارات المرافقة وطبقة الحماية
    ax2 = fig.add_subplot(122)
    gps_signal = [data['gps_snr'] for data in telemetry_data]
    
    ax2.plot(time_steps, gps_signal, label='GPS SNR Signal (dB)', color='green')
    ax2.axhline(y=15, color='r', linestyle='--', label='Jamming Threshold Line')
    
    ax2.set_title('Live Telemetry & Jamming Detection Window')
    ax2.set_xlabel('Time Step')
    ax2.set_ylabel('GPS Signal Quality')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig("flight_telemetry_analysis.png")
    print("\n📊 [Visualizer] 3D Telemetry Graph saved to 'flight_telemetry_analysis.png'.")
    plt.show()

if __name__ == "__main__":
    print("Visualizer module ready.")