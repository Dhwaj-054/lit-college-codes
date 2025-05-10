from collections import deque
def bfs(tree, start, goal):
    queue = deque([(start, [start])])  # Initialize the queue with the start node and path
    visited = set()  # Set to keep track of visited nodes
    while queue:
        node, path = queue.popleft()  # Dequeue the first element
        if node == goal:  # Check if the current node is the goal
            return path  # Return the path to the goal
        visited.add(node)  # Mark the current node as visited
        for neighbor in tree[node]:  # Iterate through the neighbors of the current node
            if neighbor not in visited:  # If the neighbor hasn't been visited
                queue.append((neighbor, path + [neighbor]))  # Enqueue the neighbor with the updated path
    return None  # Return None if the goal is not found
# Example tree represented as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
