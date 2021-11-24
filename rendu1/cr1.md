# Compte rendu intermédiaire numéro 1 - modélisation
On a dans le premier rendu le but d'avoir la même modélisation dans tous les trois problèmes fournis. Par même modélisation ça ne veut pas dire le même graphe, mais le même type de graphes et les mêmes conditions qui s'appliquent sur tous les composants du graphe. Finalement le même algorithme qu'on peut appliquer sur un certain graphe pour résoudre le problème quel que soit son type.

Dans notre modélisation on va essayer d'avoir une construction qui nous permet minimiser la complexité (de temps) de résolution du problème. Il est possible d'avoir une modélisation qui respecte les conditions déjà liste au-dessus. Mais elle n'est pas nécessairement la meilleure.

D'après la première lecture du texte on a une simple modélisation. Avec des graphes `simples` et `non-diriges` avec des `couleurs`. Mais peut-être ce n'est pas la meilleure, pour le moment et avant d'implémenter les algorithmes de résolution on va utiliser cette modélisation. L'information dans un nœud est unique. L'algorithme va changer les couleurs des nœuds.

On préfère d'avoir une haute complexité d'espace de mémoire, c'est à dire avoir des grands graphes pour décrire un certain problème, que d'avoir une haute complexité de temps, c'est à dire prendre beaucoup de temps pour le résoudre. On peut penser à l'utilisation des graphes cycliques ou à l'utilisation des graphes diriges pour rendre un problème plus facile à résoudre, par ce que ces deux types de graphes ajoute des informations/restrictions qui peuvent minimiser le nombre d’opérations à effectuer lors de la résolution.
Dans notre modélisation on doit répondre à un nombre minimal de questions.
*	C'est quoi la signification d'un nœud dans ce graphe ? `relation: noeud -> element de probleme `
*	Qu'est-ce que c'est la signification de l’information qui existe dans un nœud par rapport au problème ? `info(noeud[i]) = variable1(element[i])` 
*	Qu'est-ce que c'est la signification de la couleur d'un nœud par rapport au probleme? `couleur(noeud[i]) = variable2(element[i])`
*	Quelle est la signification d'une arête dans un certain graphe? `relation: arrete -> relation entre elements`
*	Comment résoudre le problème ? `conditions a respecter par l'algorithm de resolution`

## Modélisation du sudoku
Dans ce problème on définit:
*	Chaque `cellule` dans la grille par un `nœud`. Et ça vient du fait que chaque cellule va contenir une information spécifique a elle-même (comme pour un nœud), et donc la valeur dans le noud et la même que celle dans la cellule.
```
(noed == cellule) : info_noeud --> coord_cellule; couleur_noeud --> valeur_cellule
```
*	Les cellules qui appartiennent au `même bloque, ligne, colonne` sont tous relie (DIRECTEMENT) par une `arête`. Par ce qu’il est impossible qu’ils ont tous la même valeur on est obligée de déterminer la relation entre eux. Si une cellule est avec une autre dans le même bloque ou ligne ou colonne c'est n'est pas nécessaire de définir le type de relation ou de traiter les différents types de relations de manières différentes par ce que finalement ils subissent tous la même condition (de ne pas avoir la même valeur).
*	La condition qui existe entre les nœuds DIRECTEMENT lies est que c'est impossible pour eux d'avoir la même couleur.
## Modélisation du coloriage de cartes
Dans ce problème on définit :
*	Chaque `pays` dans la carte par un `nœud`. Et ça vient du fait que chaque pays a un nom unique qui sert comme un id et donc l'information dans le nœud. L'autre information que l'algorithme va essayer de déterminer pour résoudre le problème est la couleur de pays et donc la couleur du nœud et la même que celle du pays.
```
(noed == pays) : info_noeud --> nom_pays; couleur_noeud --> couleur_pays 
```
*	Les pays qui sont relie directement par une `frontière` (ont une frontière commune) sont relie par une `arête` dans le graphe. Car c'est impossible d'avoir des pays directement lies qui ont la même couleur.
*	La condition qui existe entre les nœuds DIRECTEMENT lies est que c'est impossible pour eux d'avoir la même couleur. (Même condition que celle en haut)

## Modélisation de l'attribution de fréquences
Dans ce problème on définit :
*	Chaque `antenne` par un `nœud`. On peut imaginer qu’une antenne a un ID ou coordonnées unique, même chose pour l'information dans son nœud.
```
(noed == antenne) : info_noeud --> coord_antenne; couleur_noeud --> fréquence_antenne
```
*	Les `antennes voisines` sont reliées DIRECTEMENT par une `arête` dans le graphe. Car c'est impossible d'avoir des antennes directement lies qui ont la même fréquence.
*	La condition qui existe entre les nœuds DIRECTEMENT lies est que c'est impossible pour eux d'avoir la même couleur. (Même condition que celle en haut)

## Problème commun
*	Colorier les nœuds directement lies par des couleurs différentes 😄 .

J'ai cru qu'il y aura un algorithme complètement diffèrent des problèmes qui le décris indirectement, trouver le plus proche voisin par exemple pour résoudre le problème. Mais la modélisation n'est pas très différente, on est censé colorer les nœuds (comme dans le 2eme problème les pays).

On peut trouver une solution en traversant le graphe plusieurs fois avec un certain nombre minimum de couleurs et a chaque fois on colorie le maximum nombre de nœuds possible avec une certaine couleur. Le nombre des fois à traverser un graphe sera le même que de couleurs ? Comment déterminer le nombre minimal de couleurs à avoir ? avec le nombre maximal d'arrêt d'un nœud dans tout le graphe ?
Citations

