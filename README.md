# NavAI: Advanced 12-DOF Drone Dynamics & Anti-Jamming System

NavAI est un environnement de simulation hybride haute performance conçu pour tester la dynamique de vol de drones et les algorithmes de navigation anti-brouillage basés sur l'IA.

## 🏗️ Architecture du Système

Le projet est structuré en deux modules complémentaires :
1. **Moteur de dynamique de vol C++ (`/src`, `/include`)** : Modèle mathématique à 12 degrés de liberté (12-DOF) calculant la position, la vitesse et l'orientation avec la bibliothèque `Eigen`.
2. **Module d'IA Python (`/ai_module`)** : Pipeline d'IA traitant la télémétrie, corrigeant les interférences de signal et affichant la trajectoire en temps réel.

## 📂 Structure du Projet

```text
nav_ai_project/
├── ai_module/
│   ├── anti_jamming.py
│   └── visualizer.py
├── build/
│   └── flight_dynamics.exe
├── include/
│   └── drone_dynamics.hpp
├── src/
│   └── main.cpp
├── README.md
└── run_full_system.py
```

## 🚀 Compilation et Exécution

### 1. Compilation du moteur C++
```powershell
g++ -O3 -I ./eigen -I ./eigen/eigen-3.4.0 src/main.cpp -o build/flight_dynamics.exe
```

### 2. Lancement du système complet
```powershell
python run_full_system.py
```

