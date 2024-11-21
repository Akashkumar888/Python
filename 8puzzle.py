
from queue import PriorityQueue

def heuristic(start, goal):
    return sum(abs(s // 3 - g // 3) + abs(s % 3 - g % 3) for s, g in zip(start, goal))

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print("\n")

def a_star_8_puzzle(start, goal):
    pq = PriorityQueue()
    pq.put((0, start, 0, -1))  # (priority, current state, depth, previous blank index)
    visited = set()
    visited.add(tuple(start))

    while not pq.empty():
        _, current, depth, blank_idx = pq.get()

        if current == goal:
            print("Solution found in", depth, "steps:")
            print_puzzle(current)
            return

        for direction in [-1, 1, -3, 3]:
            new_blank = blank_idx + direction if blank_idx != -1 else current.index(0) + direction
            if 0 <= new_blank < 9 and (direction == -1 and new_blank % 3 < 2) or (direction == 1 and new_blank % 3 > 0):
                new_state = current[:]
                new_state[current.index(0)], new_state[new_blank] = new_state[new_blank], new_state[current.index(0)]
                
                if tuple(new_state) not in visited:
                    visited.add(tuple(new_state))
                    priority = depth + 1 + heuristic(new_state, goal)
                    pq.put((priority, new_state, depth + 1, new_blank))

    print("No solution exists.")

# Example
start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print("8-Puzzle Problem:")
a_star_8_puzzle(start_state, goal_state)

