from collections import deque

def water_jug_problem(jug1, jug2, target):
    visited = set()  # To store visited states
    queue = deque([(0, 0, [])])  # Start with both jugs empty and an empty path
    visited.add((0, 0))

    while queue:
        x, y, path = queue.popleft()
        
        # If we reach the target amount in either jug
        if x == target or y == target:
            return path + [(x, y)]

        # Generate all possible states
        states = [
            (jug1, y, path + [(x, y)]),  # Fill jug1
            (x, jug2, path + [(x, y)]),  # Fill jug2
            (0, y, path + [(x, y)]),     # Empty jug1
            (x, 0, path + [(x, y)]),     # Empty jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y), path + [(x, y)]),  # Pour jug1 -> jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x), path + [(x, y)])   # Pour jug2 -> jug1
        ]

        for state in states:
            next_state = (state[0], state[1])
            if next_state not in visited:
                visited.add(next_state)
                queue.append(state)

    return None

# Example Usage
if __name__ == "__main__":
    jug1 = 4
    jug2 = 3
    target = 2
    result = water_jug_problem(jug1, jug2, target)
    
    if result:
        print(f"Target {target} liters is achievable. Steps:")
        for step in result:
            print(step)
    else:
        print(f"Target {target} liters is not achievable.")
