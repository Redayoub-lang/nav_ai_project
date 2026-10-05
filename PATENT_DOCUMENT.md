@'
# DEMANDE DE BREVET D'INVENTION

## TITRE
SYSTÈME ET PROCÉDÉ DE NAVIGATION HYBRIDE TEMPS RÉEL POUR AÉRONEF SANS PILOTE (UAV) À 12 DEGRÉS DE LIBERTÉ AVEC COMMUTATION AUTO-ADAPTATIVE ANTI-BROUILLAGE GPS.
1. DOMAINE TECHNIQUE
La présente invention concerne le domaine de la navigation autonome pour véhicules aériens non habités (UAV), et plus particulièrement un système logiciel et matériel permettant le maintien de trajectoire lors d'interférences ou de déni de signal GPS/GNSS.

2. ÉTAT DE LA TECHNIQUE ET PROBLÈME RÉSOLU
Les systèmes de navigation conventionnels pour drones reposent fortement sur les signaux GPS. En cas d'attaque par brouillage electromagnétique, la perte du signal entraîne une dérive rapide ou un crash. Les méthodes d'intégration inertielle classiques accumulent une erreur quadratique importante au cours du temps. La présente invention résout ce problème en combinant un moteur dynamique à 12 degrés de liberté (12-DOF) à un filtrage hybride auto-adaptatif (EKF / Dead Reckoning) activé sous un seuil critique d'allure Signal-sur-Bruit (SNR < 15 dB).

3. REVENDICATIONS (CLAIMS)
Revendication Indépendante 1 (Système)
Un système de navigation hybride anti-brouillage pour aéronef sans pilote (UAV) à 12 degrés de liberté (12-DOF), caractérisé en ce qu'il comprend :

Un moteur physique calculant en temps réel la dynamique de vol selon 12 variables d'état : x = [x, y, z, vx, vy, vz, phi, theta, psi, p, q, r]^T

Un module de détection précoce d'interférences mesurant en continu le rapport Signal-sur-Bruit (SNR) du récepteur satellite.

Un filtre d'estimation de position auto-adaptatif configuré pour basculer automatiquement d'un mode de correction GPS nominal à un mode d'estimation inertielle prédictive lorsque le SNR passe sous un seuil prédéterminé de 15 dB.

Revendication Dépendante 2 (Procédé)
Procédé de maintien de trajectoire mis en œuvre par le système de la revendication 1, caractérisé par les étapes suivantes :

Capture de la télémétrie de vol et évaluation du niveau de SNR à chaque pas de temps dt.

Comparaison du SNR avec la valeur de consigne 15 dB.

Si SNR >= 15 dB : Réalignement de la matrice de covariance de position sur les données satellitaires.

Si SNR < 15 dB : Suspension des mises à jour satellitaires et calcul de la position prédite via le Filtre de Kalman Étendu.

Revendication Dépendante 3 (Analyse & Diagnostic)
Procédé selon la revendication 2, caractérisé en ce qu'il génère un rapport horodaté au format CSV enregistrant les positions brutes, les positions corrigées, le SNR et l'état binaire du brouillage pour l'auditabilité et le diagnostic de vol post-mission.