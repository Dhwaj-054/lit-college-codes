# this is the python code for Iterative deepening depth first search in AI 

graph = {}
n = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))

for _ in range(e):
  u, v = map(int, input("Enter edge (u, v): ").split())
  if u not in graph:
    graph[u] = []
  if v not in graph: 
    graph[v] = []
 graph[u].append(v)
 graph[v].append(u) 
start = int(input("Enter the start node: "))
goal = int(input("Enter the goal node: "))
path = []

found = False
for limit in range(len(graph)): 
 visited = set() 
 stack = [(start, [start])]
 while stack:
 node, current_path = stack.pop()
 if node == goal: 
 path = current_path
 found = True
 break
 if len(current_path) <= limit: 
 visited.add(node)
 for neighbor in graph.get(node, []):
 if neighbor not in visited:
 stack.append((neighbor, current_path + [neighbor]))
 if found: 
 break

if found:
 print(f"Path exists from {start} to {goal}.")
 print("Path:", " -> ".join(map(str, path)))
else:
 print(f"No path exists from {start} to {goal}.")
