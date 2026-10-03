import os
import subprocess
import time

def run_integration_test():
    print("===================================================")
    print(" 🚀 STARTING [nav_ai] FULL SYSTEM INTEGRATION TEST ")
    print("===================================================\n")

    # الخطوة 1: تجميع كود C++ (محرك الفيزياء)
    print(">> [1/3] Compiling C++ Flight Dynamics Engine...")
    compile_cmd = "g++ -std=c++20 -O3 src/main.cpp -I ./eigen -o build/nav_ai.exe"
    compilation_result = os.system(compile_cmd)
    
    if compilation_result != 0:
        print("❌ Error: C++ Compilation failed!")
        return

    time.sleep(1)

    # الخطوة 2: تشغيل محرك الطيران واستخراج البيانات
    print("\n>> [2/3] Launching UAV Physics Simulation (C++ Executable)...")
    print("-" * 50)
    
    # تشغيل ملف C++ وقراءة مخرجاته
    process = subprocess.Popen(['build\\nav_ai.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # طباعة بيانات الطيران لحظياً
    for line in process.stdout:
        print(f"✈️ {line.strip()}")
        time.sleep(0.1) # تأخير بسيط لمحاكاة الزمن الفعلي
    
    print("-" * 50)
    print(">> UAV Simulation Completed. Gathering Telemetry Data...")
    time.sleep(2)

    # الخطوة 3: تمرير البيانات لنظام الذكاء الاصطناعي لفحص التشويش
    print("\n>> [3/3] Activating AI Anti-Jamming Module (Python)...")
    print("-" * 50)
    os.system("python ai_module/anti_jamming.py")
    
    print("\n===================================================")
    print(" ✅ FULL SYSTEM INTEGRATION TEST COMPLETED! ")
    print("===================================================")

if __name__ == "__main__":
    run_integration_test()