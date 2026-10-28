graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}


def astar(start, goal):
    open_list = [(start, 0)]
    come_from = {}
    g_cost = {start: 0}

    while open_list:
        current_node_with_cost = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )

        open_list.remove(current_node_with_cost)
        current_node = current_node_with_cost[0]

        if current_node == goal:
            path = [goal]

            while current_node in come_from:
                current_node = come_from[current_node]
                path.append(current_node)

            path.reverse()
            return path, g_cost[goal]

        for neighbour, cost in graph[current_node]:
            new_cost = g_cost[current_node] + cost

            if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_cost
                come_from[neighbour] = current_node
                open_list.append((neighbour, new_cost))

    return None, float("inf")


start = input("Enter the start node: ").strip().upper()
goal = input("Enter the goal node: ").strip().upper()

path, cost = astar(start, goal)

if path:
    print("Shortest path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("Path not found")