from sys import stdin, stderr
import traceback


def posisjoner(ord, node):
    ind = []
    if '?' in ord:
        indexList = [n for n in xrange(len(ord)) if ord.find('?', n) == n]
        if len(indexList) > 0:
            for y in node:
                if len(ord) == len(y[0]):
                    mutatedString = list(y[0])
                    for x in xrange(len(indexList)):
                        mutatedString[indexList[x]] = "?"
                    if ''.join(mutatedString) == ord:
                        ind.append(y[1])
    else:
        for x in node:
            if x[0] == ord:
                ind.append(x[1])
    return ind


try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append((o, pos))
        pos += len(o) + 1
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, ordliste)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)