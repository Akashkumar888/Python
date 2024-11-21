
def minimax(depth, node_index, is_maximizer, scores, height):
    if depth == height:
        return scores[node_index]

    if is_maximizer:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height),
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height),
        )

# Example usage
scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3  # Total levels in the tree
print("Optimal value:", minimax(0, 0, True, scores, height))

