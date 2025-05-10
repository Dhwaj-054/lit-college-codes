# a star with tree input
import heapq

def a_star_search(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))  # (f = g+h, g, node, path)
    closed_set = set()

    while open_list:
        f, g, current_node, path = heapq.heappop(open_list)

        if current_node == goal:
            return path, g  # Found goal

        closed_set.add(current_node)

        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in closed_set:
                new_g = g + cost
                new_f = new_g + heuristics.get(neighbor, float('inf'))
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found

# --- Input Section ---
graph = {}
n = int(input("Enter number of nodes: "))
print("Enter the edges in format: parent child cost")
for _ in range(int(input("Enter number of edges: "))):
    u, v, c = input().split()
    c = int(c)
    if u in graph:
        graph[u].append((v, c))
    else:
        graph[u] = [(v, c)]

heuristics = {}
print("Enter heuristic values for each node (node h):")
for _ in range(n):
    node, h = input().split()
    heuristics[node] = int(h)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# --- Run A* Search ---
path, cost = a_star_search(graph, heuristics, start, goal)

# --- Output ---
if path:
    print("Path found:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found from", start, "to", goal)
