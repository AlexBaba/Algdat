__author__ = 'Sondre'
from sys import stdin


def minCoinsGreedy(coins, value):
    total_sum = 0
    coin_counter = 0
    index_ = 0
    while total_sum != value:
        if total_sum + coins[index_] <= value:
            total_sum += coins[index_]
            coin_counter += 1
            index_ = 0
        else:
            index_ += 1
    return coin_counter


def minCoinsDynamic(coins, value):
    C = [0]
    for p in xrange(1, value + 1):
        best_cost = Inf
        for c in coins:
            if c <= p:
                cost = 1 + C[p - c]
                if cost < best_cost:
                    best_cost = cost
        C.append(best_cost)
    return C[value]


def canUseGreedy(coins):
    for x in xrange(len(coins) - 1):
        if coins[x] % coins[x + 1] == 0:
            continue
        else:
            return False
    return True


Inf = 1000000000
coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
    for line in stdin:
        print minCoinsGreedy(coins, int(line))
else:
    for line in stdin:
        print minCoinsDynamic(coins, int(line))