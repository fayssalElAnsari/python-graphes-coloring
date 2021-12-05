# Compte rendu intermédiaire numéro 2 - algorithmes

## Rappel du problème commun
*	Colorier les nœuds directement lies par des couleurs différentes 😄 .

On peut trouver une solution en traversant le graphe plusieurs fois avec un certain nombre minimum de couleurs et a chaque fois on colorie le maximum nombre de nœuds possible avec une certaine couleur. Le nombre des fois à traverser un graphe sera le même que de couleurs ? Comment déterminer le nombre minimal de couleurs à avoir ? avec le nombre maximal d'arrêt d'un nœud dans tout le graphe ? Nous allons utiliser le back tracking.

## De la difficulté de résoudre le problème
### Explication de ce qu’on entend par un probleme difficile:
* on veut dire ici par un probleme difficile un probleme ou c'est difficile de savoir s'il existe une solution avant de faire le calcul,
* Il existe plusieurs solutions possibles.
* dans des cas differents il est possible d'avoir un algorithm optimal different 
  
### definition d'une heuristique:
* c'est une maniere pour resoudre un probleme qui est tres similaire a l'essaye-erreur/brute force. Il n'existe pas d'un seul algorithm optimal pour trouver la solution.


## Algorithme naïf
L'algorithm naif proposee est de parcourir l'arbre une premiere fois pour trouver le nombre maximale de neodus qui est relier a un autre noeud dans tout le graphe.
Et apres on va avoir le nombre de couleurs a utiliser. Apres cette premiere etape il est possible de faire un entre deux choix. Le premier consiste a parcourir l'arbre autant de fois
qu'on a de couleurs pour a chaque fois colorier les neouds autant que possible. En respectant la condition de ne pas avoir deux nueods adjacent qui ont la meme couleur. L'autre choix consiste a parcourir le graphe une seul fois en faisant le choix de couleur d'une liste ordonne. En commancant par la premiere couleur si c'est pas possible de colorier le noeud avec cetter couleur on essaye si la deuxieme couleur dans la liste est possible et ainsi de suite.

### Idée    
On commence par l'hyposthese qu'il existe une solution et on commence a tester. Et si on peut pas colorier un noeud avec un des couleurs qu'on a dans la liste on peut dire que le probleme n'a pas de solution meme si la possibilite d'avoir une solution dans ce cas depend des choix d'ordre des couleurs.

### Algorithme


### Complexité


## Algorithme heuristique

### Idée

### Algorithme

Sous forme de pseudocode.

### Complexité

### Limites

## Citations

Si vous utilisez des éléments lus par ailleurs, citez vos sources.
