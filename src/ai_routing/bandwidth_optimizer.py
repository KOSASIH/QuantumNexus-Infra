import numpy as np

class BandwidthOptimizer:
    def __init__(self):
        self.bandwidth_matrix = None

    def set_bandwidth_matrix(self, matrix):
        """Set the bandwidth matrix for the network."""
        self.bandwidth_matrix = matrix

    def optimize(self, path):
        """Optimize the bandwidth along the given path."""
        if self.bandwidth_matrix is None:
            raise ValueError("Bandwidth matrix not set.")

        min_bandwidth = float('inf')
        for i in range(len(path) - 1):
            node_a = path[i]
            node_b = path[i + 1]
            min_bandwidth = min(min_bandwidth, self.bandwidth_matrix[node_a][node_b])

        optimized_path = []
        for i in range(len(path)):
            optimized_path.append(path[i])
            if i < len(path) - 1:
                optimized_path.append(f"({min_bandwidth})")  # Indicate bandwidth along the path

        return optimized_path

if __name__ == "__main__":
    # Example bandwidth matrix
    bandwidth_matrix = [
        [0, 10, 5, 0, 0, 0],
        [10, 0, 5, 15, 5, 0],
        [5, 5, 0, 10, 10,  0],
        [0, 15, 10, 0, 0, 20],
        [0, 5, 10, 0, 0, 15],
        [0, 0, 0, 20, 15, 0]
    ]

    optimizer = BandwidthOptimizer()
    optimizer.set_bandwidth_matrix(bandwidth_matrix)
    path = [0, 1, 2, 4]
    optimized_path = optimizer.optimize(path)
    print(f"Optimized path: {optimized_path}")
