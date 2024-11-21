
def alpha_beta_pruning(depth, node_index, is_maximizer, scores, alpha, beta, height):
    if depth == height:
        return scores[node_index]

    if is_maximizer:
        value = float("-inf")
        for i in range(2):  # Two children
            value = max(
                value,
                alpha_beta_pruning(
                    depth + 1, node_index * 2 + i, False, scores, alpha, beta, height
                ),
            )
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for i in range(2):  # Two children
            value = min(
                value,
                alpha_beta_pruning(
                    depth + 1, node_index * 2 + i, True, scores, alpha, beta, height
                ),
            )
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

# Example usage
scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3  # Total levels in the tree
print("Optimal value:", alpha_beta_pruning(0, 0, True, scores, float("-inf"), float("inf"), height))

