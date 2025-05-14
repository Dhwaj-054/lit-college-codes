import heapq

# Graph in the form: node: [(neighbor, cost), ...]
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 12)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 3)],
    'F': [('G', 3)],
    'G': []
}

# Heuristic values (h(n)) – estimated cost from node to goal
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 0
}

def a_star(start, goal):
    # Priority queue: (f_score, current_node, path_taken, g_cost)
    open_list = [(heuristic[start], start, [start], 0)]

    while open_list:
        f, current, path, g = heapq.heappop(open_list)

        if current == goal:
            print("Path:", " -> ".join(path))
            print("Total cost:", g)
            return

        for neighbor, cost in graph[current]:
            g_new = g + cost
            f_new = g_new + heuristic[neighbor]
            heapq.heappush(open_list, (f_new, neighbor, path + [neighbor], g_new))

    print("No path found.")

# Example usage
a_star('A', 'G')
