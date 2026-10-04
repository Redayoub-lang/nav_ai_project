# NavAI: Advanced 12-DOF Drone Dynamics & Anti-Jamming System

NavAI est un environnement de simulation hybride haute performance conçu pour tester la dynamique de vol de drones et les algorithmes de navigation anti-brouillage basés sur l'IA.

## 🏗️ Architecture du Système

Le projet est structuré en deux modules complémentaires :
1. **Moteur de dynamique de vol C++ (`/src`, `/include`)** : Modèle mathématique à 12 degrés de liberté (12-DOF) calculant la position, la vitesse, l'orientation et les vitesses angulaires avec la bibliothèque `Eigen`.
2. **Module d'IA Python (`/ai_module`)** : Pipeline d'intelligence artificielle traitant les données de télémétrie, corrigeant les interférences de signal et affichant la trajectoire en temps réel.

## 📂 Structure du Projet

```text
nav_ai_project/
├── ai_module/
│   ├── anti_jamming.py       # Algorithmes d'IA anti-brouillage et filtrage
│   └── visualizer.py         # Visualisation graphique de la trajectoire
├── build/
│   └── flight_dynamics.exe   # Exécutable du moteur physique
├── eigen/                    # Bibliothèque C++ Eigen (algèbre linéaire)
├── include/
│   └── drone_dynamics.hpp    # Modèle physique 12-DOF
├── src/
│   └── main.cpp              # Point d'entrée C++
├── README.md                 # Documentation du projet
└── run_full_system.py        # Script maître liant le C++ et Python
⚙️ Prérequis
Environnement C++ : Compilateur g++ (GCC) et Eigen 3.4.0

Environnement Python : Python 3.8+, numpy, matplotlib

🚀 Compilation et Exécution
1. Compilation du moteur C++
PowerShell
g++ -O3 -I ./eigen -I ./eigen/eigen-3.4.0 src/main.cpp -o build/flight_dynamics.exe
2. Lancement du système complet
PowerShell
python run_full_system.py