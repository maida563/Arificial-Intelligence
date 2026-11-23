# ========================================================================
# ===============================Minimax==================================
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': -1,
    'I': 4,
    'J': 2,
    'K': 6,
    'L': -3,
    'M': -5,
    'N': 0,
    'O': 7,
}


def minimax(node, depth, maximizingPlayer):
    # if depth == 0 or node is a terminal node then return static evaluation of node
    if depth == 0 or isinstance(tree[node], int):
        # Checks for the leaf node that has Integer value
        # Returns the value(int) 
        return tree[node]

    if maximizingPlayer:  # for Maximizer Player
        maxEva = float('-inf')
        for child in tree[node]:
            eva = minimax(child, depth - 1, False)
            # MaxEva current high score, eva returns the child high score
            maxEva = max(maxEva, eva)
        return maxEva

    else:  # for Minimizer player
        minEva = float('inf')
        for child in tree[node]:
            eva = minimax(child, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva


# Initial call: Minimax(node, depth, Player(min or max))
result = minimax('A', 3, True)
print('Optimal Value (Minimax):', result)

# =======================================================================
# ======================= Alpha Beta Pruning=============================
# Tree representation using a dictionary (matching the example on pages 2-4)
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['D1', 'D2'],
    'E': ['E1', 'E2'],
    'F': ['F1', 'F2'],
    'G': ['G1', 'G2'],
    'D1': 3,
    'D2': 5,
    'E1': 6,
    'E2': 9,
    'F1': 1,
    'F2': 2,
    'G1': 0,
    'G2': -1,
}


def minimax_alpha_beta(node, depth, isMaximizingPlayer, alpha, beta):
    # if node is a leaf node: return value of the node
    if isinstance(game_tree[node], int):
        return game_tree[node]

    if isMaximizingPlayer:
        bestVal = float('-inf')
        for child in game_tree[node]:
            value = minimax_alpha_beta(child, depth + 1, False, alpha, beta)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal

    else:
        bestVal = float('inf')
        for child in game_tree[node]:
            value = minimax_alpha_beta(child, depth + 1, True, alpha, beta)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal


# Initial call: minimax(node, 0, true, -INFINITY, +INFINITY)
result = minimax_alpha_beta('A', 0, True, float('-inf'), float('inf'))
print('Optimal Value (Alpha-Beta Pruning):', result)