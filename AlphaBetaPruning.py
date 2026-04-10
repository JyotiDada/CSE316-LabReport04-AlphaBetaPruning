import random
import math

class Counter:
    def __init__(self):
        self.count = 0

class ABCounter:
    def __init__(self):
        self.visited = 0
        self.pruned = 0

def generate_leaf_nodes(n):
    return [random.randint(1, 25) for _ in range(n)]

def minimax(depth, index, is_max, values, max_depth, counter):
    counter.count += 1
    if depth == max_depth:
        return values[index]
    if is_max:
        return max(
            minimax(depth + 1, index * 2, False, values, max_depth, counter),
            minimax(depth + 1, index * 2 + 1, False, values, max_depth, counter)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True, values, max_depth, counter),
            minimax(depth + 1, index * 2 + 1, True, values, max_depth, counter)
        )

def alpha_beta(depth, index, is_max, values, max_depth, alpha, beta, counter):
    counter.visited += 1
    if depth == max_depth:
        return values[index]
    if is_max:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, False, values, max_depth, alpha, beta, counter)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                counter.pruned += 1
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, True, values, max_depth, alpha, beta, counter)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                counter.pruned += 1
                break
        return best

def main():
    n = 8
    values = generate_leaf_nodes(n)
    print("Generated Leaf Nodes:", values)

    depth = int(math.log2(n))

    c1 = Counter()
    res1 = minimax(0, 0, True, values, depth, c1)

    print("\nMinimax:")
    print("    Nodes Evaluated:", c1.count)
    print("    Optimal Value:", res1)

    c2 = ABCounter()
    res2 = alpha_beta(0, 0, True, values, depth, -math.inf, math.inf, c2)

    print("\nAlpha-Beta Pruning:")
    print("    Nodes Evaluated:", c2.visited)
    print("    Nodes Pruned:", c2.pruned)
    print("    Optimal Value:", res2)

    improvement = ((c1.count - c2.visited) / c1.count) * 100
    print("\nEfficiency Improvement: {:.2f}%".format(improvement))

if __name__ == "__main__":
    main()