import numpy as np
import random
from bandwidth_optimizer import BandwidthOptimizer

class RoutingAlgorithm:
    def __init__(self, network_topology):
        self.network_topology = network_topology  # Adjacency matrix representation
        self.bandwidth_optimizer = BandwidthOptimizer()

    def find_shortest_path(self, source, destination):
        """Find the shortest path using Dijkstra's algorithm."""
        num_nodes = len(self.network_topology)
        visited = [False] * num_nodes
        distances = [float('inf')] * num_nodes
        previous_nodes = [None] * num_nodes

        distances[source] = 0

        for _ in range(num_nodes):
            min_distance_node = self._get_min_distance_node(distances, visited)
            visited[min_distance_node] = True

            for neighbor in range(num_nodes):
                if (self.network_topology[min_distance_node][neighbor] > 0 and
                        not visited[neighbor]):
                    new_distance = distances[min_distance_node] + self.network_topology[min_distance_node][neighbor]
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous_nodes[neighbor] = min_distance_node

        return self._reconstruct_path(previous_nodes, source, destination)

    def _get_min_distance_node(self, distances, visited):
        """Helper function to get the node with the minimum distance."""
        min_distance = float('inf')
        min_index = -1
        for i in range(len(distances)):
            if distances[i] < min_distance and not visited[i]:
                min_distance = distances[i]
                min_index = i
        return min_index

    def _reconstruct_path(self, previous_nodes, source, destination):
        """Reconstruct the path from source to destination."""
        path = []
        current_node = destination
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        path.reverse()
        return path

    def optimize_bandwidth(self, path):
        """Optimize bandwidth for the given path."""
        optimized_path = self.bandwidth_optimizer.optimize(path)
        return optimized_path

if __name__ == "__main__":
    # Example network topology (adjacency matrix)
    network_topology = [
        [0, 1, 4, 0, 0, 0],
        [1, 0, 4, 2, 7, 0],
        [4, 4, 0, 3, 5, 0],
        [0, 2, 3, 0, 0, 6],
        [0, 7, 5, 0, 0, 7],
        [0, 0, 0, 6, 7, 0]
    ]
    
    routing = RoutingAlgorithm(network_topology)
    path = routing.find_shortest_path(0, 4)
    print(f"Shortest path from 0 to 4: {path}")
    optimized_path = routing.optimize_bandwidth(path)
    print(f"Optimized path: {optimized_path}")
