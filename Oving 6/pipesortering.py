__author__ = 'Sondre'
from sys import stdin
import math
import random


# Randomized Quicksort
def sorter(A):
    less = []
    equal = []
    greater = []
    if len(A) > 1:
        pivot = A[random.randint(0, len(A) - 1)]
        for x in A:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sorter(less) + equal + sorter(greater)
    else:
        return A

# Binearsok med rekursjon
def binary_search(A, verdi):
    size = len(A)
    mid_index = int(math.floor(len(A) / 2))
    if len(A) < 2 and A[0] != verdi:
        return A[0]
    if A[mid_index] == verdi:
        return verdi
    else:
        if A[mid_index] > verdi:
            A = A[0:mid_index]
        elif A[mid_index] < verdi:
            A = A[mid_index:size]
        return binary_search(A, verdi)

def finn(A, nedre, ovre):
    n = 0
    nedre_grense = binary_search(A, nedre)
    ovre_grense = binary_search(A, ovre)

    if ovre > A[-1]:
        ovre_grense = A[-1]
    else:
        while ovre_grense < ovre:
            n += 1
            ovre_grense = binary_search(A, A[A.index(ovre_grense) + n])
    if nedre < A[0]:
        nedre_grense = A[0]
    resultat = [nedre_grense, ovre_grense]
    return resultat

liste = []
for x in stdin.readline().split():
    liste.append(int(x))

sortert = sorter(liste)
for linje in stdin:
    ord = linje.split()
    minst = int(ord[0])
    maks = int(ord[1])
    resultat = finn(sortert, minst, maks)
    print str(resultat[0]) + " " + str(resultat[1])