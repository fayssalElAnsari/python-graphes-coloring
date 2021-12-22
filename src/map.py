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
    with open(".\\exemples\\"+inputfile) as f:
        lines = f.read().splitlines()
        for i in range(len(lines)):
            lines[i] = tuple(lines[i].split(" "))
    G.add_edges_from(lines)
    nx.set_node_attributes(G, None, "color")
    algo_naif(G)
    algo_test(G)

if __name__ == "__main__":
   main(sys.argv[1:])



# algo_backtracking(G)
