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

## I. Algorithme test
L'algorithm naif proposee est de parcourir l'arbre une premiere fois pour trouver le nombre maximale de neodus qui est relier a un autre noeud dans tout le graphe.
Et apres on va avoir le nombre de couleurs a utiliser. Apres cette premiere etape il est possible de faire un entre deux choix. Le premier consiste a parcourir l'arbre autant de fois
qu'on a de couleurs pour a chaque fois colorier les neouds autant que possible. En respectant la condition de ne pas avoir deux nueods adjacent qui ont la meme couleur. L'autre choix consiste a parcourir le graphe une seul fois en faisant le choix de couleur d'une liste ordonne. En commancant par la premiere couleur si c'est pas possible de colorier le noeud avec cetter couleur on essaye si la deuxieme couleur dans la liste est possible et ainsi de suite. Cette maniere prend en compte le fait qu'on doit avoir la liste des couleurs au debut de l'execution du programme. En utilisant C par exemple c'est plus facile. Mais comme nous allons utiliser Python on peur utiliser les listes et une liste de couleurs variables.

### Idée    
On commence par l'hyposthese qu'il existe une solution et on commence a tester. Et si on peut pas colorier un noeud avec un des couleurs qu'on a dans la liste on peut dire que le probleme n'a pas de solution meme si la possibilite d'avoir une solution dans ce cas depend des choix d'ordre des couleurs.

### Algorithme
###### ce n'est pas necessaire de savoir la liste de couleurs qu'on va utiliser en evance.
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
il suffit de parcourir le graphe une seul foix en largeur et donc a partir du pseudocode, dans le pire des cas: O(c*v)

### II. Algorithm naif
### Idée  
Générez toutes les configurations de couleurs possibles. Étant donné que chaque nœud peut être coloré à l'aide de n'importe laquelle des m couleurs disponibles, le nombre total de configurations de couleurs possibles est: de c^V.
Après avoir généré une configuration de couleur, vérifiez si les sommets adjacents ont la même couleur ou non. Si les conditions sont remplies, imprimez la combinaison et rompez la boucle.

### Algorithme
1. Créez une fonction récursive qui prend l'indice actuel, le nombre de sommets et le tableau de couleurs de sortie.
2. Si l'index courant est égal au nombre de sommets. Vérifiez si la configuration de la couleur de sortie est sûre, c'est-à-dire vérifiez si les sommets adjacents n'ont pas la même couleur. Si les conditions sont remplies, imprimez la configuration et cassez.
3. Attribuez une couleur à un sommet (1 à c).
4. Pour chaque couleur attribuée, appelez récursivement la fonction avec l'indice suivant et le nombre de sommets
5. Si une fonction récursive retourne vrai, interrompez la boucle et retourne vrai.

### Complexité
* Comme on gerene la liste complete des toute les combinaisons possible et on va les tester, le complexite de temps sera: O(c^V)

### Pseudocode 
```python
# pour tester si le graphe avec la coloration actuelle est une solution
est_correct(g):
    # pour chaque arete
    pour arete in g.aretes:
            si (arete[0].couleur == arete[1].color): #si les deux nueods de l'aretes ont la meme couleur donc c'est incorrecte
                return False
    return True

colorier_graph(g, max, i, couleurs):
    si (i == max):
        si (est_correct(g)):
            imprimer_solution(g)#une fonction quelquonque pour imprimer la solution
            return True
        return False
    pour noeud in graph.noeuds:
        pour j in range(1, max + 1):
            noeud.color= couleurs[i]
            if (colorier_graph(g, m, i + 1, couleurs)):
                return True
            couleurs[i] = 0
    return False



```

## III. Algorithme heuristique
AKA Backtracking 

### Idée
Pour avoir un nombre minimal des couleurs a utiliser, nous allons utiliser le backtracking c'est a dire: lorsque on prend la liste qui est la difference entre les deux listes les coueleurs deja utilisee et les couleurs des voisins, si la liste contient plus qu'un seul element on est obligee de faire un choix entre ces plusieurs couleurs. En meme temps si on ne peut pas utiliser aucune des couleurs c'est a dire la liste est vide, ce resultat est une consequence des choix anterieurs qu'on a fait. Donc on peut relier ces deux affirmations pour avoir dire que si on a choisis la deuxieme couleur par exemple au lieu de la premiere nous seront pas obligee d'ajouter une nouvelle couleur pour resoudre le probleme.

Finalement pour etre sur d'avoir un nombre minimal de couleurs a chaque resolution on peut garder une historique de nos choix faites et les choix possibles et avant d'ajouter une nouvelle couleur on peut revenir pour modifier notre choix et a chaque fois on revient encore jusqu'au premier noeud si on essaye tout les decisions possibles on peut dire que le faite que l'algorithm est bloque ne depend pas de nos choix et donc il faut absolument ajouter une couleur pour resoudre le probleme.

### Algorithme
Sous forme de pseudocode.

### Complexité
Le pire des cas est le meme par ce que dans le pire des cas nous allons tester toutes les combinaisons possible de coloriage: O(c^v) mais le temps en moyenne de plusieurs resolutions sera moins que dans le cas de l'algorithm naif pratiquement.

### Limites
Le probleme avec le backtracking sans ordoner les couleurs est qu'on peut resoudre le probleme dans une duree tres courte ou tres longue. Avec un choix de couleur aleatoire il n'y a pas beaucoup de place pour l'amélioration. Donc il faut reflechir a ordoner les couleurs a choisir et les noeuds a colorier par degree, et colorier le graph par ordre decroissant des noeuds.

## Citations
Cours graphes - Jean Stephane VAREE - chapitre II   
https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/ Pour l'alogo naif
