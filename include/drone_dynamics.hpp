#pragma once

#include <iostream>
#include <cmath>
#include <Eigen/Dense>

namespace nav_ai {

class DroneDynamics {
public:
    using StateVector = Eigen::Matrix<double, 12, 1>;
    using ControlVector = Eigen::Matrix<double, 4, 1>;

    DroneDynamics() : mass(1.2), gravity(9.81) {}

    StateVector compute_derivatives(const StateVector& x, const ControlVector& u) const {
        StateVector dxdt = StateVector::Zero();
        
        double total_thrust = u.sum();
        
        // Z-axis dynamics
        dxdt(2) = x(8); // dz/dt = w
        dxdt(8) = (total_thrust / mass) - gravity; // acceleration z
        
        return dxdt;
    }

private:
    double mass;
    double gravity;
};

} // namespace nav_ai
