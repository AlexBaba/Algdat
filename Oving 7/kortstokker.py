__author__ = 'Sondre'
from sys import stdin
from itertools import repeat
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


def merge(decks):
    tupple_list = [x for b in decks for x in b]
    index_list = [h[0] for h in tupple_list]
    sorted_list = sorter(index_list)
    sorted_decks = [z[1] for x in sorted_list for z in tupple_list if z[0] == x]
    return ''.join(sorted_decks)

decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print merge(decks)