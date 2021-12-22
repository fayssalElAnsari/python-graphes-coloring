#!/usr/bin/python

from algorithms import *
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("script.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("test.py -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    G = nx.Graph()
    for i in range(1, 10):
        for j in range(1, 10):
            G.add_node(i+9*(j-1), color=None , pos=(i, j))

    # apply colors from file
    with open('.\\exemples\\sudoku_1.txt') as f:
        lines = f.read().splitlines()
        for i in range(len(lines)):
            lines[i] = tuple(lines[i].split(" "))
    for i, j, k in zip(lines[0], lines[1], lines[2]):
        G.add_node(int(i)+9*(int(j)-1), pos=(int(i), int(j)), color=k)

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

    # algo_naif(G) #bcp de temps pour generer tous les permutations
    algo_test(G)
    algo_backtracking(G)


if __name__ == "__main__":
   main(sys.argv[1:])
   