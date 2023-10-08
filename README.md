# self-driving-rides
Hashcode 2018

## Auteur
Colin de Seroux
<br>
Adresse e-mail : phenix333.dev@gmail.com

## Description
Ce programme est une application Python utilisant la bibliothèque tkinter pour créer une interface graphique permettant de visualiser les trajets effectués par des véhicules autonomes dans un environnement donné. Les données des trajets sont lues à partir d'un fichier d'entrée (`*.txt`) et les trajets effectués sont lus à partir d'un fichier de sortie (`ends_*.txt`).

## Fonctionnalités

- Affichage des trajets effectués par les véhicules sous forme de lignes colorées sur un canevas.
- Possibilité de zoomer et de dézoomer pour une meilleure visualisation.
- Défilement horizontal et vertical pour explorer l'ensemble de la carte.
- Affichage de la légende pour interpréter les couleurs des trajets.
- Détection des trajets non attribués et affichage dans la console.

## Utilisation
1. Assurez-vous d'avoir les fichiers `*.txt` (fichier d'entrée) et `ends_*.txt` (fichier de sortie) dans le même répertoire que ce programme.
2. Exécutez le programme en exécutant le script Python.
3. Utilisez les touches de votre clavier pour effectuer les actions suivantes :
   - `+` : Zoomer (agrandir)
   - `-` : Dézoomer (réduire)
   - Flèche gauche : Défiler vers la gauche
   - Flèche droite : Défiler vers la droite
   - Flèche haut : Défiler vers le haut
   - Flèche bas : Défiler vers le bas

## Exemple de légende des couleurs des trajets

- Trajets inatteignables : Jaune
- Bonus inatteignable : Bleu
- Bonus atteignable : Vert

## Avertissement
Ce programme est destiné à des fins de visualisation et de démonstration uniquement. Il ne garantit pas la précision ou la validité des données des trajets. Les trajets non attribués sont détectés et affichés dans la console, mais il est conseillé de vérifier les données à des fins d'analyse plus poussée.

## Remarques
Ce code utilise la bibliothèque tkinter pour créer l'interface graphique. Assurez-vous d'avoir tkinter installé sur votre système pour exécuter ce programme.

## Au dessus de 300 trajets c'est compliqué / il ne faut pas être préssé
Si vous avez des idées d'optimisation ...
