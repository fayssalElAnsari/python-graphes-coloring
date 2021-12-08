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
qu'on a de couleurs pour a chaque fois colorier les neouds autant que possible. En respectant la condition de ne pas avoir deux nueods adjacent qui ont la meme couleur. L'autre choix consiste a parcourir le graphe une seul fois en faisant le choix de couleur d'une liste ordonne. En commancant par la premiere couleur si c'est pas possible de colorier le noeud avec cetter couleur on essaye si la deuxieme couleur dans la liste est possible et ainsi de suite. Cette maniere prend en compte le fait qu'on doit avoir la liste des couleurs au debut de l'execution du programme. En utilisant C par exemple c'est plus facile. Mais comme nous allons utiliser Python on peur utiliser les listes et une liste de couleurs variables.

### Idée    
On commence par l'hyposthese qu'il existe une solution et on commence a tester. Et si on peut pas colorier un noeud avec un des couleurs qu'on a dans la liste on peut dire que le probleme n'a pas de solution meme si la possibilite d'avoir une solution dans ce cas depend des choix d'ordre des couleurs.

### Algorithme
###### ce n'est pas necessaire de savoir la liste de couleurs qu'on va utiliser avant en evance.
1. On parcours le graphe soit en largeur soit en profondeur, tout en gardant une trace de la liste des couleurs qu'on a deja utilise. 
2. Pour chaque noeud nous allons essayer de le colorier avec les couleurs qu'on a deja utilise si c'est impossible de le faire (il existe un noeud voisin de ce noeud colorier avec la meme couleur => on passe au suivant) on va ajouter une nouvelle couleur et l'ajouter a la liste des couleurs deja utilisee.

### Pseudocode 
```python
#avec un parcours en largeur
colorier(G, départ, déjà_visités= NIL )
    si déjà_visités = NIL alors déjà_visités ← tableau(G.nombre_sommets(), FAUX );
    a_traiter ← file();
    a_traiter.enfiler(départ);
    couleurs_utilises ← liste();
    tant que a_traiter.pas_vide() faire
        couleurs_voisins ← getCouleursVoisins();
        sommet ← a_traiter.défiler();
        si ¬ déjà_visités[sommet] alors
            couleur = (couleurs_utilises - couleurs_voisins)[0]:
                si couleur:
                    sommet.colorier(couleur)
                    couleurs_utilises.enfiler(couleur)
                else:
                    nouveau_couleur = getNextNewCouleur()
                    couleurs_utilises.enfiler(nouveau_couleur)
                    sommet.colorier(nouveau_couleur)
                    
            déjà_visités[sommet] ← VRAI ;
            pour chaque voisin dans G.voisins(sommet) faire
                si ¬ déjà_visités[voisin] alors a_traiter.enfiler(voisin) ;
    return couleurs_utilises
```

### Complexité
il suffit de parcourir le graphe une seul foix en largeur donc 

## Algorithme heuristique

### Idée

### Algorithme
Sous forme de pseudocode.

### Complexité

### Limites

## Citations

Si vous utilisez des éléments lus par ailleurs, citez vos sources.
