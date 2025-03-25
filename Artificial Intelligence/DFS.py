# DFS algorithm code in python for AI

print("DFS")

def dfs(tree, start, goal):

stack = [(start, [start])] 
node and path
visited = set()

while stack:
node, path = stack.pop()

if node == goal:
  return path 

visited.add(node)

node as key and children as values
for neighbor in tree.get(node, []):
  if neighbor not in visited:
    stack.append((neighbor, path + [neighbor]))
  
  return None 
  
# Example tree structure
tree = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': [],
'F': []
 }

start_node = 'A'
goal_node = 'E'

path = dfs(tree, start_node, goal_node)

if path:
  print("Path found:", path)
else:
  print("No path found.")
