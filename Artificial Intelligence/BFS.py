#this contains the Breadth First Search algorithm code in Python language for the topic of AI using graph input

print("BFS")
from collections import deque

def bfs(graph, start, goal):

queue = deque([(start, [start])]) 
with start node and path
visited = set()

while queue:
node, path = queue.popleft()

if node == goal:
return path 

visited.add(node)

for neighbor in graph[node]:
  if neighbor not in visited:
queue.append((neighbor, path +
[neighbor])) 

return None 

# Example graph represented as a dictionary
graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
 }

start_node = 'A'
goal_node = 'F'

path = bfs(graph, start_node, goal_node)

if path:
print("Path found:", path)
else:
print("No path found.")
