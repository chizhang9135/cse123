import heapq

# This function will use Dijkstra's algorithm to find the shortest path from a start node to all other nodes in the graph
def dijkstra(graph, start):
    # Create a priority queue to store the nodes to be visited
    queue = [(0, start, [])]
    heapq.heapify(queue)

    # This dictionary will store the cost to reach each node and the path to get there
    visited = {start: (0, [])}

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        path = path + [node]

        # Visit all the neighbors of the current node
        for next_node in graph[node]:
            new_cost = cost + graph[node][next_node]
            # If the next node has not been visited or we found a cheaper path to it, update the cost and path
            if next_node not in visited or new_cost < visited[next_node][0]:
                visited[next_node] = (new_cost, path)
                heapq.heappush(queue, (new_cost, next_node, path))

    # Return a dictionary with the minimum cost and path to each node
    return visited

# Define the graph from the network topology
graph = {
    'A': {'B': 2, 'C': 8},
    'B': {'C':4, 'D': 2},
    'C': {'B': 1, 'D': 5, 'E': 6},
    'D': {'E': 3},
    'E': {'A': 5, 'D': 1}
}

# Calculate the shortest paths from router A to all other routers
shortest_paths_a = dijkstra(graph, 'A')

# Calculate the shortest paths from router B to all other routers
shortest_paths_b = dijkstra(graph, 'B')

routers = ['A', 'B', 'C', 'D', 'E']
shortest_paths = {}
routing_tables = {}

for router in routers:
    # Calculate the shortest paths from current router to all other routers
    shortest_paths[router] = dijkstra(graph, router)

    # Extract the routing table for current router
    routing_tables[router] = {
        destination: (path[1] if len(path) > 1 else destination, cost)
        for destination, (cost, path) in shortest_paths[router].items()
        if destination != router
    }

    print(f"\nRouter: {router}")
    print("Shortest Paths:")
    for destination, (cost, path) in shortest_paths[router].items():
        print(f"  To {destination}: Cost = {cost}, Path = {' -> '.join(path)}")

    print("Routing Table:")
    for destination, (next_router, cost) in routing_tables[router].items():
        print(f"  To {destination}: Next Router = {next_router}, Cost = {cost}")
