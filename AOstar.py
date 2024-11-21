
class Graph:
    def __init__(self):
        self.graph = {}
        self.status = {}
        self.solution = {}

    def add_node(self, name, children):
        self.graph[name] = children
        self.status[name] = "unresolved"
        self.solution[name] = None

    def get_min_cost(self, name):
        min_cost = float("inf")
        best_child = None
        for children, cost in self.graph[name]:
            total_cost = cost + sum(self.solution[child] for child in children)
            if total_cost < min_cost:
                min_cost = total_cost
                best_child = children
        return min_cost, best_child

    def ao_star(self, node):
        if self.status[node] == "resolved":
            return self.solution[node]

        for children, cost in self.graph[node]:
            for child in children:
                if self.status[child] == "unresolved":
                    self.ao_star(child)

        min_cost, best_child = self.get_min_cost(node)
        self.solution[node] = min_cost
        self.status[node] = "resolved"
        return min_cost

# Example graph
g = Graph()
g.add_node("A", [(["B", "C"], 2), (["D"], 1)])
g.add_node("B", [(["E"], 3)])
g.add_node("C", [(["F"], 2)])
g.add_node("D", [])
g.add_node("E", [])
g.add_node("F", [])

print("AO* Optimal Cost:", g.ao_star("A"))
