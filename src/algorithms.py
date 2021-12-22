import networkx as nx
from networkx.classes import graph
import matplotlib.pyplot as plt
import networkx as nx
import itertools

# will need a way to define a none color ? either color="None" or just remove the color attribute?
# c'est mieux d'utiliser des entiers pour definir les couleurs au lieu d'utiliser les couleurs directement

# colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'navy', 'slateblue']
# colors_nb = {}
# keys = range (1,len(colors))
# for i in keys:
#     colors_nb[i] = colors[i-1]
colors = range(0, 100)

def animate_graph(G):
    color_map = []
    for node in G.nodes:
        color_map.append(G.nodes[node]['color'])
    if nx.get_node_attributes(G, 'pos'):
        pos=nx.get_node_attributes(G,'pos')
        nx.draw(G, pos, node_color=color_map, with_labels=True, font_weight='bold')
    else:
        nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
    plt.show(block=False)
    plt.pause(0.01)
    plt.close()

# apply the color from the graph attributes
def show_graph(G):
    color_map = []
    for node in G.nodes:
        color_map.append(G.nodes[node]['color'])
    if nx.get_node_attributes(G, 'pos'):
        pos=nx.get_node_attributes(G,'pos')
        nx.draw(G, pos, node_color=color_map, with_labels=True, font_weight='bold')
    else:
        nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
    plt.show()

def print_graph(G):
    if nx.get_node_attributes(G, 'pos'):
        for node in G.nodes:
            print(G.nodes[node]['pos'][0], G.nodes[node]['pos'][1], G.nodes[node]["color"])
    else:
        for node in G.nodes:
            print(node, G.nodes[node]["color"])

### ALGORITHM TEST ###
def algo_test(G):
    color_map = []
    nx.set_node_attributes(G, 0, "color")

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
        animate_graph(G)
        color_map.append(unused_colors[0])

    show_graph(G) 
    print_graph(G)

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
    nx.set_node_attributes(G, 0, "color")
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
            animate_graph(G)
            correct = is_correct(G)
            if(correct):
                break
        i = i + 1

    show_graph(G) 
    print_graph(G) 

### BACKTRACKING ###
# the question is how can we keep track of the choices we have made?
# each time we reach a dead-end (meaning the list of possible colors is empty)
# we will fall back, each time we fall back we need to revert the color of the
# previous node to the first color in the colors list (revert all changes)
# instead of keeping track of all the list of previously used colors for each node
# we simply need to have an ordered list of possible colors, when we fall back to
# a node we will increment to the next color, therefore we need to get the index 
# of the current color, increment it by 1, get the corresponding color, apply it 
# to the current node and go to the next one

# another problem is the fact that the nodes are not ordered by relation in G.nodes
# meaning we need to apply a breadth first search/depth first search to color the graph
def algo_backtracking(G):
    color_map = []
    nx.set_node_attributes(G, "white", "color")

    node_index = 0
    correct = False
    max_colors = 1
    usable_colors = range(1, max_colors)

    nodes_list = list(G.nodes())
    while not correct and node_index < G.number_of_nodes():
        neighbors_colors = []
        for neighbor in G.neighbors(nodes_list[node_index]):
            if len(G.nodes[neighbor]) > 0:
                neighbors_colors.append(G.nodes[neighbor]['color'])
            # the list is empty we should fall back
                
        unused_colors = [c for c in usable_colors if (c not in neighbors_colors)]
        if len(unused_colors) > 0:
            G.nodes[nodes_list[node_index]]['color'] = unused_colors[0]
            color_map.append(unused_colors[0])
        else:
            if node_index > 0:
                G.nodes[nodes_list[node_index]]['color'] = ""
                node_index = node_index - 1
                G.nodes[nodes_list[node_index]]['color'] = G.nodes[nodes_list[node_index]]['color'] + 1
            else:
                max_colors = max_colors + 1
                usable_colors = range(1, max_colors)
        print(usable_colors)

    show_graph(G) 
    print_graph(G)

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