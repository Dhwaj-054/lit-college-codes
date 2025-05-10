from collections import deque

def bfs(tree, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    print("BFS Traversal Order:")
    while queue:
        node, path = queue.popleft()
        print(f"Visiting: {node}")

        if node == goal:
            return path

        visited.add(node)

        for neighbor in tree.get(node, []):
            if neighbor not in visited and all(neighbor != n for n, _ in queue):
                queue.append((neighbor, path + [neighbor]))

    return None

def parse_tree_input():
    print("Enter tree nodes and their children in the format:")
    print("Node: Child1 Child2 Child3")
    print("Enter an empty line to finish input.\n")

    tree = {}
    while True:
        line = input("Enter node and children: ").strip()
        if line == "":
            break
        if ':' not in line:
            print("Invalid format, please use 'Node: Child1 Child2 ...'")
            continue
        node_part, children_part = line.split(':', 1)
        node = node_part.strip()
        children = children_part.strip().split() if children_part.strip() else []
        tree[node] = children

    return tree

def main():
    tree = parse_tree_input()
    if not tree:
        print("No tree entered. Exiting.")
        return

    start_node = input("Enter start node: ").strip()
    goal_node = input("Enter goal node: ").strip()

    if start_node not in tree:
        print(f"Start node '{start_node}' not found in tree.")
        return
    # goal node can be leaf or non-leaf, if not in tree keys, check if in any children
    nodes_all = set(tree.keys())
    children_all = set(c for children in tree.values() for c in children)
    if goal_node not in nodes_all and goal_node not in children_all:
        print(f"Goal node '{goal_node}' not found in tree.")
        return

    path = bfs(tree, start_node, goal_node)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()

