#pragma once

#include <iostream>
#include <cmath>
#include <Eigen/Dense>

namespace nav_ai {

class DroneDynamics {
public:
    using StateVector = Eigen::Matrix<double, 12, 1>;
    using ControlVector = Eigen::Matrix<double, 4, 1>;

    DroneDynamics() : mass(1.5), gravity(9.81), Lo(0.25) {
        I << 0.01165, 0.0, 0.0,
             0.0, 0.01165, 0.0,
             0.0, 0.0, 0.02332;
    }

    StateVector compute_derivatives(const StateVector& x, const ControlVector& u) const {
        StateVector dxdt = StateVector::Zero();

        double phi = x(6);   // Roll
        double theta = x(7); // Pitch
        double psi = x(8);   // Yaw
        double p = x(9);    // Roll rate
        double q = x(10);  // Pitch rate
        double r = x(11);   // Yaw rate

        double Db = u.sum();
        double Tau_phi = Lo * (u(1) - u(3));
        double Tau_theta = Lo * (u(2) - u(0));
        double Tau_psi = 0.01 * (u(0) - u(1) + u(2) - u(3));

        dxdt(0) = x(3);
        dxdt(1) = x(4);
        dxdt(2) = x(5);

        dxdt(3) = (cos(phi)* sin(theta)* cos(psi) + sin(phi)* sin(psi)) * Db / mass;
        dxdt(4) = (cos(phi)*sin(theta)* sin(psi) - sin(phi)* cos(psi)) * Db / mass;
        dxdt(5) = (cos(phi)*cos(theta) * Db / mass) - gravity;

        dxdt(6) = p + sin(phi)*tan(theta)*q + cos(phi)*tan(theta)*r;
        dxdt(7) = cos(phi)*q - sin(phi)*r;
        dxdt(8) = sin(phi)/cos(theta)*q + cos(phi)/cos(theta)*r;

        Eigen::Vector3d omega(p, q, r);
        Eigen::Vector3d tau(Tau_phi, Tau_theta, Tau_psi);
        Eigen::Vector3d omega_dot = I.inverse() * (tau - omega.cross(I * omega));

        dxdt(9) = omega_dot(0);
        dxdt(10) = omega_dot(1);
        dxdt(11) = omega_dot(2);

        return dxdt;
    }

private:
    double mass;
    double gravity;
    double Lo; 
    Eigen::Matrix3d I;
};

}
