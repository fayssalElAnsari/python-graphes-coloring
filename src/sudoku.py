from algorithms import *

G = nx.Graph()
with open('gsm1.txt') as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        lines[i] = tuple(lines[i].split(" "))
    print(lines)
G.add_edges_from(lines)

algo_test(G)

algo_naif(G)

algo_backtracking(G)

