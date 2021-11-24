# Compte rendu intermédiaire numéro 1 - modélisation
    
On a dans le premier rendu le but d'avoir la meme modelisation dans tout les trois problemes fournis. Par meme modelisation ca veut pas dire le meme graphe, mais le meme type de graphes et les meme conditions qui s'appliquent sur tout les composants du graphe.Finalement le meme algorithm qu'on peut appliquer sur un certain graphes pour resoudre le probleme quelque soit son type.

Dans notre modelisation on va essayer d'avoir une construction qui nous permet minimiser la complexite (de temps) de resolution du probleme. Il est possible d'avoir une modelisation qui respecte les conditions deja liste au dessus. Mais elle n'est pas necessairement la meilleure.

D'apres la premiere lecture du texte on a une simple modelisation. Avec des graphes `simples` et `non-diriges`. Mais peut etre ce n'est pas la meilleure, pour le moment et avant d'implementer les algorithmes de resolution on va utiliser cette modelisation. 

On prefere d'avoir une haute complexite d'espace de memoire, c'est a dire avoir des grandes graphes pour decrire un certain probleme, que d'avoir une haute complexite de temps, c'est a dire prendre beaucoup de temps pour le resoudre. On peut penser a l'utilisation des couleurs ou a l'utilisation des graphes diriges pour rendre un probleme plus facile a resoudre, par ce que ces deux types de graphes ajoute des informations/restrictions qui peuvent minimiser le nombre d'operations a effectuer lors de la resolution.

Dans notre modelisation on doit repondre a un nombre minimale de questions.
* C'est quoi la signification d'un noeud dans ce graphe? `relation: noeud -> element de probleme` 
* Quelle est la signification d'une arette dans un certain graphe? `relation: arrete -> element de probleme` 
* Comment resoudre le probleme? `algorithm de resolution`

## Modélisation du sudoku
Dans ce probleme on definie:
* Chaque `cellule` dans la grille par un `noeud`. Et ca vient du faite que chaque cellule va contenir une information specifique a elle meme (comme pour un noeud). 

* Les cellules qui appartient au `meme bloque, ligne, colonne` sont tous relie par une `arrete`. Par ce que il est impossible qui'il sont tous  

## Modélisation du coloriage de cartes


## Modélisation de l'attribution de fréquences


## Problème commun


## Citations


Si vous utilisez des éléments lus par ailleurs, citez vos sources.
