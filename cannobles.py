from collections import deque

def is_valid_state(m_left, c_left, boat_left, m_right, c_right):
    # Check if state is valid (no side should have more cannibals than missionaries)
    if m_left >= 0 and c_left >= 0 and m_right >= 0 and c_right >= 0:
        if (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right):
            return True
    return False

def missionaries_and_cannibals():
    # Initial state: 3 missionaries, 3 cannibals on the left bank
    start = (3, 3, 1, 0, 0)  # (m_left, c_left, boat_left, m_right, c_right)
    goal = (0, 0, 0, 3, 3)  # Goal state

    visited = set()
    queue = deque([(start, [])])  # (current_state, path)
    visited.add(start)

    while queue:
        current_state, path = queue.popleft()
        m_left, c_left, boat_left, m_right, c_right = current_state

        # If we reach the goal state
        if current_state == goal:
            return path + [goal]

        # Generate all possible next states
        if boat_left:  # If the boat is on the left bank
            moves = [(-1, 0), (0, -1), (-2, 0), (0, -2), (-1, -1)]
        else:  # If the boat is on the right bank
            moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

        for m, c in moves:
            new_state = (
                m_left - m * boat_left,
                c_left - c * boat_left,
                1 - boat_left,
                m_right + m * boat_left,
                c_right + c * boat_left
            )
            if new_state not in visited and is_valid_state(*new_state):
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))

    return None  # No solution

def describe_state(state):
    m_left, c_left, boat_left, m_right, c_right = state
    description = (
        f"Left bank: {m_left} missionaries, {c_left} cannibals | "
        f"Boat: {'left' if boat_left else 'right'} | "
        f"Right bank: {m_right} missionaries, {c_right} cannibals"
    )
    return description

# Enhanced Example Usage
if __name__ == "__main__":
    solution = missionaries_and_cannibals()
    if solution:
        print("\nSolution Path:")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}: {describe_state(state)}")
    else:
        print("No solution found.")
 