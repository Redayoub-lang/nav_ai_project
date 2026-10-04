#include <iostream>
#include "../include/drone_dynamics.hpp"

int main() {
    std::cout << "=========================================\n";
    std::cout << "[nav_ai] Advanced 12-DOF Flight Dynamics Engine\n";
    std::cout << "=========================================\n\n";

    nav_ai::DroneDynamics drone;
    nav_ai::DroneDynamics::StateVector state = nav_ai::DroneDynamics::StateVector::Zero();
    nav_ai::DroneDynamics::ControlVector control;
    
    // ضبط سرعات المحركات الأربعة لتوليد رفع وتوجيه زاوية بسيط
    control << 3.8, 3.6, 3.8, 3.6; 

    double dt = 0.01;
    for (int step = 0; step <= 50; ++step) {
        if (step % 10 == 0) {
            std::cout << "Step " << step 
                      << " | Pos (X,Y,Z): (" << state(0) << ", " << state(1) << ", " << state(2) << ")"
                      << " | Roll: " << state(6) * 57.2958 << " deg"
                      << " | Pitch: " << state(7) * 57.2958 << " deg\n";
        }
        nav_ai::DroneDynamics::StateVector state_derivative = drone.compute_derivatives(state, control);
        state += state_derivative * dt;
    }

    std::cout << "\n[nav_ai] 12-DOF Physics Engine Test Complete.\n";
    return 0;
}
