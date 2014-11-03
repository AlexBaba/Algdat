__author__ = 'Sondre'
from sys import stdin, maxint


def korteste_rute(rekkefolge, nabomatrise, byer):
    all_to_all = floyd_warshall(nabomatrise, byer)
    path_sum = 0
    current_node = rekkefolge[0]
    for y in rekkefolge:
        path_sum += all_to_all[current_node][y]
        current_node = y
    path_sum += all_to_all[current_node][rekkefolge[0]]
    if path_sum >= maxint:
        return "umulig"
    else:
        return path_sum


def floyd_warshall(nabomatrise, byer):
    dist = nabomatrise
    for k in xrange(byer):
        for i in xrange(byer):
            for j in xrange(byer):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


testcases = int(stdin.readline())
for test in range(testcases):
    byer = int(stdin.readline())
    rekkefolge = [int(by) for by in stdin.readline().split()]
    nabomatrise = []
    for by in range(byer):
        rad = []
        for x in stdin.readline().split():
            x = int(x)
            if x == -1:
                x = maxint
            rad.append(x)
        nabomatrise.append(rad)
    print korteste_rute(rekkefolge, nabomatrise, byer)
