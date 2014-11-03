from sys import stdin

def run():

    rl = stdin.readline
    rl()
    rl()
    r = rl()
    rn = str(rl().strip())
    d = 0
    ll = [l.split() for l in stdin]
    while int(rn) != int(r):
        for sl in ll:
            if rn in sl and rn != sl[0]:
                rn = sl[0]
                ll.remove(sl)
                break
        d += 1
    print d

    return
run()
