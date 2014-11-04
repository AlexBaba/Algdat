W = 740
v = [18, 27, 49, 40, 24, 22, 29, 10, 24, 40]
w = [320, 301, 371, 296, 303, 359, 148, 275, 296, 395]
n = len(v)

def solve_knapsack(w, v, i, W):
    if i == 0:
        if w[i] <= W:
            return v[i]
        else:
            return 0
    candidate_1 = solve_knapsack(w, v, i - 1, W)
    if w[i] > W:
        return candidate_1
    else:
        candidate_2 = v[i] + solve_knapsack(w, v, i - 1, W - w[i])
    return max(candidate_2, candidate_1)

print(solve_knapsack(w, v, n - 1, W))
