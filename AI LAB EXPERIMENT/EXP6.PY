import math

def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta, height):
    if depth == height:
        return values[node_index]

    if maximizing_player:
        best = -math.inf
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, height)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
    else:
        best = math.inf
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, height)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
    return best


values = list(map(int, input("Enter leaf node values: ").split()))

height = 3

result = alpha_beta(0, 0, True, values, -math.inf, math.inf, height)

print("The optimal value is:", result)