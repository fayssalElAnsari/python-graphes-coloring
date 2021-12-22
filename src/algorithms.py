import networkx as nx
from networkx.classes import graph
import matplotlib.pyplot as plt
import networkx as nx
import itertools

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

# apply the color from the graph attributes
# for node in G.nodes:
#     color_map.append(G.nodes[node]['color'])

### ALGORITHM TEST ###
def algo_test(G):
    color_map = []
    nx.set_node_attributes(G, colors[1], "color")

    # coloring graph
    # first get the list of colors of neighbors
    # subtract the colors of neibors from the colors already in colors
    # chose the first color of the new colors list to be applied to the current node
    # do this for all the graph's nodes :)
    for node in G.nodes:
        neighbors_colors = []
        for neighbor in G.neighbors(node):
            if len(G.nodes[neighbor]) > 0:
                neighbors_colors.append(G.nodes[neighbor]['color'])
        unused_colors = [c for c in colors if (c not in neighbors_colors)]
        G.nodes[node]['color'] = unused_colors[0]
        color_map.append(unused_colors[0])

    nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
    plt.show()  

### ALGORITHM NAIF ###
# une fonction pour verifier que la coloration est correcte:
# on regarde les couleurs tout les voisins du neod actuel par rapport a son couleur
# si les couleur sont differente donc la coloration correct :)
# on a le probleme de choix de couleurs, on commence par une couleur et a la fin de 
# la boucle on ajoute une autre jusqu'on trouve un solution 
# def is_correct(graph):
#     for edge in graph.edges:
#         if(G[edge[0]]['color'] == G[edge[1]]['color']):
#             return False
#         return True
def is_correct(graph):
    for node in graph.nodes:
        for neighbor in graph.neighbors(node):
            if(graph.nodes[node]['color'] == graph.nodes[neighbor]['color']):
                return False
    return True

def algo_naif(G):   
    nx.set_node_attributes(G, colors[1], "color")
    color_map = []
    used_colors = []
    # on a le probleme de generer une permutation de n couleurs avec n la taille du graphe
    # pour cela nous allons utiliser: itertools.permutations(used_colors, n) 
    # pour repetition product et repeat 
    n = G.number_of_nodes()
    i = 0
    correct = False
    while not correct and i < G.number_of_nodes():
        used_colors.append(colors[i])
        permutations = list(itertools.product(used_colors, repeat=n))
        for permutation in permutations:
            for node, color in zip(G.nodes, permutation):
                G.nodes[node]['color'] = color
            # print(G.nodes.data())
            color_map = permutation
            correct = is_correct(G)
            if(correct):
                break
        i = i + 1


    nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
    plt.show() 

### BACKTRACKING ###
def algo_backtracking(G):
    color_map = []
    nx.set_node_attributes(G, colors[1], "color")

    node_index = 0
    color_index = 0
    correct = False

    nodes_list = list(G.nodes())
    while not correct and node_index < G.number_of_nodes():
        neighbors_colors = []
        for neighbor in G.neighbors(G.nodes[nodes_list[node_index]]):
            if len(G.nodes[neighbor]) > 0:
                neighbors_colors.append(G.nodes[neighbor]['color'])
            # the list is empty we should fall back
                
        unused_colors = [c for c in colors if (c not in neighbors_colors)]
        if len(unused_colors) > 0:
            G.nodes[nodes_list[node_index]]['color'] = unused_colors[0]
            color_map.append(unused_colors[0])
        else:
            node_index = node_index - 1

    nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
    plt.show() 

# nx.set_node_attributes(G, colors[1], "color")
# color_map = []

# used_colors = []
# n = G.number_of_nodes()
# i = 0
# correct = False
# while not correct and i < G.number_of_nodes():
#     used_colors.append(colors[i])
#     permutations = list(itertools.product(used_colors, repeat=n))
#     for permutation in permutations:
#         for node, color in zip(G.nodes, permutation):
#             G.nodes[node]['color'] = color
#         # print(G.nodes.data())
#         color_map = permutation
#         correct = is_correct(G)
#         if(correct):
#             break
#     i = i + 1

# nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
# plt.show()