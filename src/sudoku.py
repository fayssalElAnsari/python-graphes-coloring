from algorithms import *

G = nx.Graph()

# empty nodes
for i in range(9):
    for j in range(9):
        G.add_node(i+j*9, color=None , pos=(i, j))

# apply colors from file
with open('..\\sudoku_1.txt') as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        lines[i] = tuple(lines[i].split(" "))
for i, j, k in zip(lines[0], lines[1], lines[2]):
    G.add_node(int(i)+int(j)*9, pos=(int(i), int(j)), color=colors_nb[int(k)])

# populate the graph with edges of sudoku grid
# 1. same block
# THERE IS A PROBLEM WITH THE LAST CELL
for node1 in G.nodes:
    for node2 in G.nodes:
        i1 = G.nodes[node1]['pos'][0]
        j1 = G.nodes[node1]['pos'][1]
        i2 = G.nodes[node2]['pos'][0]
        j2 = G.nodes[node2]['pos'][1]
        if ((int(i1/3) == int(i2/3) and int(j1/3) == int(j2/3 ) and (not i1+9*j1 == i2+9*j2))):
            G.add_edge(i1+j1*9, i2+j2*9) 

# 2. same column or row
for node1 in G.nodes:
    for node2 in G.nodes:
        i1 = G.nodes[node1]['pos'][0]
        j1 = G.nodes[node1]['pos'][1]
        i2 = G.nodes[node2]['pos'][0]
        j2 = G.nodes[node2]['pos'][1]
        if ((i1 == i2 or j1 == j2 ) and (not i1+9*j1 == i2+9*j2)):
            G.add_edge(i1+j1*9, i2+j2*9) 

show_graph(G)

algo_test(G)

algo_naif(G)

# algo_backtracking(G)

