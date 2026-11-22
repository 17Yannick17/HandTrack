
# Cahier des charges — HandTrack

## 1. Présentation
HandTrack est une application Python de reconnaissance
de gestes de la main en temps réel à partir d'une webcam.

## 2. Objectif
Détecter une main, analyser la position de ses doigts,
reconnaître des gestes prédéfinis et afficher une réaction
visuelle.

## 3. Exigences fonctionnelles
- F01 : Capturer le flux vidéo de la webcam.
- F02 : Détecter une main et afficher ses 21 points caractéristiques.
- F03 : Compter les doigts levés (0 à 5).
- F04 : Reconnaître trois gestes : poing fermé, main ouverte
  et signe de victoire.
- F05 : Afficher le geste reconnu en temps réel.
- F06 : Déclencher une action visuelle selon le geste détecté.

## 4. Contraintes
- Langage : Python.
- Bibliothèques principales : OpenCV et MediaPipe.
- Exécution locale sur ordinateur équipé d'une webcam.
- Une seule main analysée à la fois.
- Aucun entraînement de modèle nécessaire.
- Durée cible du projet : 4 heures.

## 5. Critères d'acceptation
- La webcam peut être ouverte et fermée correctement.
- Les points de la main sont affichés sur la vidéo.
- Les gestes prévus sont reconnus dans des conditions normales.
- L'application affiche une réponse visuelle correspondant
  au geste détecté.
- L'absence de main ne provoque pas de fausse action.

## 6. Hors périmètre de la v1.0
- Reconnaissance simultanée de plusieurs mains.
- Entraînement personnalisé d'un modèle d'IA.
- Commande du volume ou d'autres applications externes.
- Enregistrement automatique des images de la webcam.
  