# Compte rendu intermédiaire numéro 1 - modélisation
    
On a dans le premier rendu le but d'avoir la meme modelisation dans tout les trois problemes fournis. Par meme modelisation ca veut pas dire le meme graphe, mais le meme type de graphes et les meme conditions qui s'appliquent sur tout les composants du graphe.Finalement le meme algorithm qu'on peut appliquer sur un certain graphes pour resoudre le probleme quelque soit son type.

Dans notre modelisation on va essayer d'avoir une construction qui nous permet minimiser la complexite (de temps) de resolution du probleme. Il est possible d'avoir une modelisation qui respecte les conditions deja liste au dessus. Mais elle n'est pas necessairement la meilleure.

D'apres la premiere lecture du texte on a une simple modelisation. Avec des graphes `simples` et `non-diriges` avec des `couleurs`. Mais peut etre ce n'est pas la meilleure, pour le moment et avant d'implementer les algorithmes de resolution on va utiliser cette modelisation. L'information dans un noeud est unique. L'algorithm va changer les couleurs des noeuds.

On prefere d'avoir une haute complexite d'espace de memoire, c'est a dire avoir des grandes graphes pour decrire un certain probleme, que d'avoir une haute complexite de temps, c'est a dire prendre beaucoup de temps pour le resoudre. On peut penser a l'utilisation des cyclic ou a l'utilisation des graphes diriges pour rendre un probleme plus facile a resoudre, par ce que ces deux types de graphes ajoute des informations/restrictions qui peuvent minimiser le nombre d'operations a effectuer lors de la resolution.

Dans notre modelisation on doit repondre a un nombre minimale de questions.
* C'est quoi la signification d'un noeud dans ce graphe? `relation: noeud -> element de probleme` 
* Qu'est ce que c'est la signification de la information qui exist dans un noeud par rapport au probleme? `info_noeud = ?`
* Qu'est ce que c'est la signification de la couleur d'un noeud par rapport au probleme? `couleur_noeud = ?`
* Quelle est la signification d'une arette dans un certain graphe? `relation: arrete -> element de probleme` 
* Comment resoudre le probleme? `algorithm de resolution/conditions`

## Modélisation du sudoku
Dans ce probleme on definie:
* Chaque `cellule` dans la grille par un `noeud`. Et ca vient du faite que chaque cellule va contenir une information specifique a elle meme (comme pour un noeud), et donc le valeur dans le neoud et le meme que celle dans la cellule. 

```
(noed == cellule) : info_noeud --> coord_cellule; couleur_noeud --> valeur_cellule
```
* Les cellules qui appartient au `meme bloque, ligne, colonne` sont tous relie (DIRECTEMENT) par une `arrete`. Par ce que il est impossible qui'ils ont tous la meme valeur on est obligee de determiner la relation entre eux. Si une cellule est avec une autre dans le meme bloque ou ligne ou colonne c'est n'est pas necessaire de definir le types de relation ou de traiter les differents types de relations de manieres differente par ce que finalement ils subit tous la meme condition (de ne pas avoir la meme valeur). 

* La condition qui existe entre les neouds DIRECTEMENT lies est que c'est impossible pour eux d'avoir la meme couleur.

## Modélisation du coloriage de cartes
Dans ce probleme on definie:
* Chaque `pays` dans la carte par un `noeud`. Et ca vient du faite que chaque pays a un nom unique qui sert comme un id et donc l'information dans le noeud. L'autre information que l'algorithm va essayer de determiner pour resoudre le probleme est la couleur de pays et donc la couleur du noeud et la meme que celle du pays. 
```
(noed == pays) : info_noeud --> nom_pays; couleur_noeud --> couleur_pays 
```

* Les pays qui sont relie directement par une `frontiere` (ont une frontiere commune) sont relie par une `arrete` dans le graphe. Car c'est impossible d'avoir des pays directement lies qui ont la meme couleur.

* La condition qui existe entre les neouds DIRECTEMENT lies est que c'est impossible pour eux d'avoir la meme couleur. (meme condition que celle en haut)

## Modélisation de l'attribution de fréquences
Dans ce probleme on definie:
* Chaque `antenne` par un `noeud` 

## Problème commun


## Citations


Si vous utilisez des éléments lus par ailleurs, citez vos sources.
