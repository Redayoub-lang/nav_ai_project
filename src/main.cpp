#include <iostream>
#include "../include/drone_dynamics.hpp"

int main()
{
    std::cout << "=========================================\n";
    std::cout << "[nav_ai] Autonomous UAV Simulation Started\n";
    std::cout << "=========================================\n\n";

    nav_ai::DroneDynamics drone;
    nav_ai::DroneDynamics::StateVector state = nav_ai::DroneDynamics::StateVector::Zero();

    nav_ai::DroneDynamics::ControlVector control;
    control << 3.5, 3.5, 3.5, 3.5;

    double dt = 0.01;

    for (int step = 0; step <= 50; step++)
    {
        nav_ai::DroneDynamics::StateVector state_derivative = drone.compute_derivatives(state, control);
        state += state_derivative * dt;

        if (step % 10 == 0)
        {
            std::cout << "Step " << step << " | Altitude (z): " << state(2)
                      << " m | Vertical Velocity (z_dot): " << state(8) << " m/s\n";
        }
    }

    std::cout << "\n[nav_ai] Simulation Completed Successfully.\n";
    return 0;
}