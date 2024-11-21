
from queue import PriorityQueue

def a_star_search(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))  # (priority, node)
    cost = {start: 0}
    path = {start: None}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            break

        for neighbor, weight in graph[current]:
            new_cost = cost[current] + weight
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                pq.put((priority, neighbor))
                path[neighbor] = current

    return reconstruct_path(path, start, goal)

def heuristic(node, goal):
    # Example: Manhattan distance for 2D grid
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(path, start, goal):
    current = goal
    route = []
    while current != start:
        route.append(current)
        current = path[current]
    route.append(start)
    route.reverse()
    return route

# Example graph (2D grid)
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((0, 1), 1), ((1, 0), 1)],
}

start = (0, 0)
goal = (1, 1)
print("Path:", a_star_search(graph, start, goal))

