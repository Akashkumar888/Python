
def hill_climbing(start, goal, neighbors, heuristic):
    current = start

    while True:
        print(f"Current: {current}, Heuristic: {heuristic(current)}")
        if current == goal:
            return current

        next_moves = neighbors(current)
        best_move = None
        best_heuristic = float("inf")

        for move in next_moves:
            h = heuristic(move)
            if h < best_heuristic:
                best_heuristic = h
                best_move = move

        if best_heuristic >= heuristic(current):
            return current  # Local maximum reached
        current = best_move

# Example: Hill Climbing on a graph
def neighbors(node):
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
    }
    return graph.get(node, [])

def heuristic(node):
    goals = {"A": 6, "B": 5, "C": 4, "D": 3, "E": 2, "F": 1, "G": 0}
    return goals.get(node, float("inf"))

start = "A"
goal = "G"
print("Goal Reached:", hill_climbing(start, goal, neighbors, heuristic))

