__author__ = 'Sondre'
from sys import *
import traceback

def subgraftetthet(nabomatrise, startnode):

    n = len(nabomatrise)

    #BFS for aa finne delgrafen til startnoden
    node_queue = [nabomatrise[startnode]]
    visited_nodes = [startnode]
    #Variabler for aa oke hastighet
    node_append = node_queue.append
    visited_append = visited_nodes.append
    #BFS
    while len(node_queue) > 0:
        rot = node_queue.pop(0)
        counter = 0
        for child in rot:
            counter += 1
            if child and counter - 1 not in visited_nodes:
                node_append(nabomatrise[counter - 1])
                visited_append(counter - 1)

    #Finner noder som ikke er del av treet til startnoden, og legger de i en liste
    sub_graph = []
    for x in xrange(n):
        if x not in visited_nodes:
            sub_graph.append(x)

    #Finner antall kanter i listen over ubesokte noder
    kanter = 0
    for e in sub_graph:
        counter = 0
        for y in nabomatrise[e]:
            counter += 1
            if y and counter-1 not in visited_nodes:
                kanter += 1

    #Returnerer tettheten til grafen basert pa antall kanter og noder som ikke
    #er besokt
    noder = len(sub_graph)
    if noder == 0 or noder == 1:
        return 0.0
    else:
        return float(kanter) / float(noder**2)

try:
    n = int(stdin.readline())
    nabomatrise = [None] * n  # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n  # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)