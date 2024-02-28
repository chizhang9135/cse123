# Define the initial distance vectors for each router
distance_vectors = {
    'A': {'A': 0, 'B': 6, 'C': 1, 'D': 3, 'E': float('inf')},
    'B': {'A': 6, 'B': 0, 'C': float('inf'), 'D': 1, 'E': 1},
    'C': {'A': 1, 'B': float('inf'), 'C': 0, 'D': 5, 'E': float('inf')},
    'D': {'A': 3, 'B': 1, 'C': 5, 'D': 0, 'E': 3},
    'E': {'A': float('inf'), 'B': 1, 'C': float('inf'), 'D': 3, 'E': 0}
}

# Define the network topology
network_topology = {
    'A': {'B': 6, 'C': 1, 'D': 3},
    'B': {'A': 6, 'D': 1, 'E': 1},
    'C': {'A': 1, 'D': 5},
    'D': {'A': 3, 'B': 1, 'C': 5, 'E': 3},
    'E': {'B': 1, 'D': 3}
}

# Apply the Bellman-Ford algorithm to update the distance vectors after one round of exchange
def update_distance_vectors(distance_vectors, network_topology):
    new_distance_vectors = {router: {} for router in distance_vectors}
    for router in distance_vectors:
        for destination in distance_vectors[router]:
            # Start with the current known distance to the destination
            min_distance = distance_vectors[router][destination]
            # Check if any neighbor provides a shorter path to the destination
            for neighbor in network_topology[router]:
                if destination in distance_vectors[neighbor]:
                    new_distance = network_topology[router][neighbor] + distance_vectors[neighbor][destination]
                    min_distance = min(min_distance, new_distance)
            new_distance_vectors[router][destination] = min_distance
    return new_distance_vectors

# Update the distance vectors for all routers
updated_distance_vectors = update_distance_vectors(distance_vectors, network_topology)
print(updated_distance_vectors)

second_round_vectors = update_distance_vectors(updated_distance_vectors, network_topology)
print(second_round_vectors)

third_round_vectors = update_distance_vectors(second_round_vectors, network_topology)
print(third_round_vectors)