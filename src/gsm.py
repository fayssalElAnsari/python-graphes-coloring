from algorithms import *

G = nx.Graph()
# os.path.dirname("..\gsm_1.txt")
with open('..\\antennes_1.txt') as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        lines[i] = tuple(lines[i].split(" "))
G.add_edges_from(lines)

algo_test(G)

algo_naif(G)

algo_backtracking(G)
