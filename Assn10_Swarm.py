import numpy as np

class AntColony:
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        Initialize the Ant Colony Optimization algorithm.
        
        Args:
            distances (2D numpy.array): Square matrix of distances. Diagonal is assumed to be np.inf.
            n_ants (int): Number of ants running per iteration.
            n_best (int): Number of best ants who deposit pheromone.
            n_iteration (int): Number of iterations.
            decay (float): Rate at which pheromone decays. The pheromone value is multiplied by decay.
            alpha (int or float): Exponent on pheromone, higher alpha gives pheromone more weight. Default=1.
            beta (int or float): Exponent on distance, higher beta give distance more weight. Default=1.
        """
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        
    def run(self):
        """
        Run the Ant Colony Optimization algorithm.
        
        Returns:
            list: Shortest path found.
            float: Length of the shortest path.
        """
        shortest_path = None
        shortest_path_length = np.inf
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path, shortest_path_length=shortest_path_length)
            shortest_path, shortest_path_length = self.get_shortest(all_paths)
            self.pheromone * self.decay            
        return shortest_path, shortest_path_length
        
    def spread_pheronome(self, all_paths, n_best, shortest_path, shortest_path_length):
        """
        Update pheromone levels on the edges based on the quality of the solutions found.
        
        Args:
            all_paths (list): List of all paths found by the ants.
            n_best (int): Number of best ants who deposit pheromone.
            shortest_path (list): Current shortest path found.
            shortest_path_length (float): Length of the current shortest path.
        """
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, path_length in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1 / self.distances[move]
    
    def gen_path_dist(self, path):
        """
        Calculate the total distance of a path.
        
        Args:
            path (list): Path represented as a list of indices.
            
        Returns:
            float: Total distance of the path.
        """
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist
    
    def gen_all_paths(self):
        """
        Generate paths for all ants.
        
        Returns:
            list: List of tuples containing paths and their lengths.
        """
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths
    
    def gen_path(self, start):
        """
        Generate a path for a single ant.
        
        Args:
            start (int): Index of the starting city.
            
        Returns:
            list: Path represented as a list of indices.
        """
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path
        
    def pick_move(self, pheromone, dist, visited):
        """
        Probabilistically select the next city to visit based on pheromone levels and distances.
        
        Args:
            pheromone (numpy.array): Pheromone levels on edges.
            dist (numpy.array): Distances from the current city to all other cities.
            visited (set): Set of indices of visited cities.
            
        Returns:
            int: Index of the next city to visit.
        """
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0 # no going back!
        move = np.random.choice(self.all_inds, 1, p= (pheromone**self.alpha * (( 1.0 / (dist + 0.0001))**self.beta)) / np.sum((pheromone**self.alpha * (( 1.0 / (dist + 0.0001))**self.beta))) )[0]
        return move
    
    def get_shortest(self, all_paths):
        """
        Get the shortest path found among all paths.
        
        Args:
            all_paths (list): List of tuples containing paths and their lengths.
            
        Returns:
            list: Shortest path found.
            float: Length of the shortest path.
        """
        all_paths = sorted(all_paths, key=lambda x: x[1])
        return all_paths[0]
    
# Example usage
if __name__ == '__main__':
    # Example distances between cities
    distances = np.array([
        [np.inf, 2, 2, 5, 7],
        [2, np.inf, 4, 8, 2],
        [2, 4, np.inf, 1, 3],
        [5, 8, 1, np.inf, 2],
        [7, 2, 3, 2, np.inf]
    ])
    
    # Initialize and run the ant colony optimization algorithm
    ant_colony = AntColony(distances, n_ants=3, n_best=1, n_iterations=100, decay=0.1, alpha=1, beta=2)
    shortest_path, shortest_path_length = ant_colony.run()
    
    print("Shortest Path:", shortest_path)
    print("Shortest Path Length:", shortest_path_length)
