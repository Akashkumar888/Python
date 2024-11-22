
def alpha_beta_pruning(depth, node_index, is_maximizer, scores, height, alpha, beta):
    # Terminal condition: if we reach the leaf node
    if depth == height:
        return scores[node_index]

    if is_maximizer:
        max_eval = float('-inf')
        # Explore the left child
        max_eval = max(
            max_eval,
            alpha_beta_pruning(depth + 1, node_index * 2, False, scores, height, alpha, beta)
        )
        alpha = max(alpha, max_eval)

        # Prune if alpha is greater than or equal to beta
        if alpha >= beta:
            return max_eval

        # Explore the right child
        max_eval = max(
            max_eval,
            alpha_beta_pruning(depth + 1, node_index * 2 + 1, False, scores, height, alpha, beta)
        )
        alpha = max(alpha, max_eval)

        return max_eval
    else:
        min_eval = float('inf')
        # Explore the left child
        min_eval = min(
            min_eval,
            alpha_beta_pruning(depth + 1, node_index * 2, True, scores, height, alpha, beta)
        )
        beta = min(beta, min_eval)

        # Prune if beta is less than or equal to alpha
        if beta <= alpha:
            return min_eval

        # Explore the right child
        min_eval = min(
            min_eval,
            alpha_beta_pruning(depth + 1, node_index * 2 + 1, True, scores, height, alpha, beta)
        )
        beta = min(beta, min_eval)

        return min_eval

# Example usage
scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3  # Total levels in the tree
alpha = float('-inf')
beta = float('inf')

print("Optimal value with Alpha-Beta Pruning:", alpha_beta_pruning(0, 0, True, scores, height, alpha, beta))
