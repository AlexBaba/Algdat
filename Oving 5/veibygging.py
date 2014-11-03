__author__ = 'Sondre H'
from sys import stdin
from collections import deque

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
    #Lager to lister; "q" - en queue, og en liste "vekt" som skal fylles med kanteverdiene vi bruker for aa danne
    #det minste treet
    q = deque(x for x in xrange(len(nm)))
    vekt = ["-" for x in xrange(len(nm))]
    vekt[0] = 0
    while q:
        #Variabeler for minsteverdi
        min_verdi = Inf
        min_verdi_index = 0
        #Setter node_index lik det forste elementet i "ko-lista" og fjerner det
        node_index = q.popleft()
        #Finner vekten av kantene mellom node_index og resten av nodene
        #Oppdaterer billigstevei til nodene om kant_verdi er mindre enn de
        #eksisterende verdiene i vekt-listen med gitt index
        for verdi_index in q:
            kant_verdi = nm[node_index][verdi_index]
            if kant_verdi < vekt[verdi_index]:
                vekt[verdi_index] = kant_verdi
        #Finner den minste verdien i lista, og indeksen.
        for n in xrange(len(q)):
            if vekt[q[n]] < min_verdi:
                min_verdi = vekt[q[n]]
                min_verdi_index = n
        if q:
            e = q[0]
            q[0] = q[min_verdi_index]
            q[min_verdi_index] = e
    #Returnerer den hoyeste vektverdien blandt elementene i lista "vekt"
    return max(vekt)

linjer = []
for str in stdin:
    linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * n
    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
    node += 1
print mst(nabomatrise)