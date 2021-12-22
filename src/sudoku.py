from algorithms import *

G = nx.Graph()

for i in range(1, 10):
    for j in range(1, 10):
        G.add_node(i+9*(j-1), color=None , pos=(i, j))

show_graph(G)

# apply colors from file
with open('..\\sudoku_1.txt') as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        lines[i] = tuple(lines[i].split(" "))
for i, j, k in zip(lines[0], lines[1], lines[2]):
    G.add_node(int(i)+9*(int(j)-1), pos=(int(i), int(j)), color=colors_nb[int(k)])
show_graph(G)

# populate the graph with edges of sudoku grid
# 1. same block
# THERE IS A PROBLEM WITH THE LAST CELL
for node1 in G.nodes:
    for node2 in G.nodes:
        i1 = G.nodes[node1]['pos'][0]
        j1 = G.nodes[node1]['pos'][1]
        i2 = G.nodes[node2]['pos'][0]
        j2 = G.nodes[node2]['pos'][1]
        if ((int((i1-1)/3) == int((i2-1)/3) and int((j1-1)/3) == int((j2-1)/3 ) and (not i1+9*j1 == i2+9*j2))):
            G.add_edge(i1+9*(j1-1), i2+9*(j2-1)) 

# 2. same column or row
for node1 in G.nodes:
    for node2 in G.nodes:
        i1 = G.nodes[node1]['pos'][0]
        j1 = G.nodes[node1]['pos'][1]
        i2 = G.nodes[node2]['pos'][0]
        j2 = G.nodes[node2]['pos'][1]
        if ((i1 == i2 or j1 == j2 ) and (not i1+9*j1 == i2+9*j2)):
            G.add_edge(i1+9*(j1-1), i2+9*(j2-1)) 

show_graph(G)

algo_test(G)

# algo_naif(G) #bcp de temps pour generer tous les permutations

# algo_backtracking(G)


