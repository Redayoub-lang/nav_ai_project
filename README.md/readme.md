# 🛸 Autonomous GPS-Denied UAV Navigation (nav_ai)

An advanced C++20 trajectory optimization and anti-jamming framework for quadrotors. Developed for high-performance aerial robotics research.

## 🧠 System Architecture
This project implements non-linear quadrotor dynamics using Eigen3. The state vector is defined as:
$$\mathbf{x} = [x, y, z, \phi, \theta, \psi, \dot{x}, \dot{y}, \dot{z}, \dot{\phi}, \dot{\theta}, \dot{\psi}]^T$$🚀 Build InstructionsRun the following commands in your terminal:Bashg++ -std=c++20 -O3 src/main.cpp -I ./eigen -o build/nav_ai.exe
.\build\nav_ai.exe

### 4. التجميع والتشغيل
افتح الـ Terminal في VS Code (`Ctrl + ~`)، وتأكد أنك داخل مجلد `nav_ai_project`، ثم قم بتشغيل الأوامر التالية بالترتيب:

```powershell
g++ -std=c++20 -O3 src/main.cpp -I ./eigen -o build/nav_ai.exe
.\build\nav_ai.exe