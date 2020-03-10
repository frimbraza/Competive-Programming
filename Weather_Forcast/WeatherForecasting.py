
# Weather Forecasting Assignment

class Weather:
    # grid properties
    grid = []
    width = 0
    height = 0

    max_label = '@'
    storm_label = '&'
    cloud_label = '.'
    default_label = '#'

    # what we need
    clusters = []

    def __init__(self, user_input=''):
        # Get user input
        if not user_input:
            user_input = input('Filename Cloud_Size: ')
        self.filename, self.cloud_size = user_input.split()
        self.cloud_size = int(self.cloud_size)
        self.read_contents(self.filename)
        print('Current Grid:')
        print(f'height: {self.height}, width: {self.width}')
        self.print_grid(self.grid)

        self.find_clusters()

        print('\nCluster Locations:')
        for cluster in self.clusters:
            print(f'Size: {cluster[0]}, Cluster: {cluster[1]}')

        new_grid = self.make_new_grid()
        print('\nNew Grid with Clusters!')
        self.print_grid(new_grid)

    def get_max_coords(self):
        max_size = 0
        max_coords = []

        for cluster in self.clusters:
            if cluster[0] > max_size:
                max_size = cluster[0]
                max_coords = cluster[1]
            elif cluster[0] == max_size:
                max_coords += cluster[1]

        return max_coords

    def threshold_coords(self):
        threshold_coords = []

        for cluster in self.clusters:
            if cluster[0] >= self.cloud_size:
                threshold_coords += cluster[1]

        return threshold_coords

    def cluster_coords(self):
        coords = []

        for cluster in self.clusters:
            coords += cluster[1]

        return coords

    # Finds a single cluster based on coord. Returns a list of coords in a cluster
    def find_cluster(self, coord):
        stack = [coord]
        cluster = []

        while stack:
            current = stack.pop()
            if current not in cluster:
                cluster.append(current)
                neighbors = [x for x in self.get_neighbors(current) if x not in cluster]
                for neighbor in neighbors:
                    stack.append(neighbor)

        return cluster

    def find_clusters(self):
        # Find the clusters and store the coordinates in a list
        visited = []
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == '.':
                    coord = (i,j)
                    if coord not in visited:
                        cluster = self.find_cluster(coord)
                        visited += cluster
                        self.clusters.append([len(cluster), cluster])

    # returns neighbors that are '.'
    def get_neighbors(self, coord):
        neighbors = []
        y = coord[0]
        x = coord[1]

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    pass
                else:
                    new_coord = (y + i, x + j)
                    if self.in_bounds(new_coord):
                        if self.grid[new_coord[0]][new_coord[1]] == self.cloud_label and new_coord != coord:
                            neighbors.append(new_coord)
        return neighbors

    # checks if a coordinate is within bounds of grid
    def in_bounds(self, coord):
        if coord[0] < 0 or coord[0] >= self.height:
            return False
        if coord[1] < 0 or coord[1] >= self.width:
            return False
        return True

    # After clusters have been found, make a new grid with proper symbols
    def make_new_grid(self):
        max_coords = self.get_max_coords()
        threshold_coords =self.threshold_coords()
        cluster_coords = self.cluster_coords()

        new_grid = []

        for i in range(self.height):
            line = ''
            for j in range(self.width):
                coord = (i,j)
                if coord in max_coords:
                    line += self.max_label
                elif coord in threshold_coords:
                    line += self.storm_label
                elif coord in cluster_coords:
                    line += self.cloud_label
                else:
                    line += self.default_label
            new_grid.append(line)

        return new_grid

    # Fix Print
    def print_grid(self, grid):
        for row in range(self.height - 1):
            print(grid[row])

    def read_contents(self, filename):
        f = open(filename, 'r+')
        line = f.readline()
        while line:
            if '\n' in line:
                line = line[:-1]
            self.grid.append(line)
            line = f.readline()
        self.height = len(self.grid)
        self.width = len(self.grid[0])              # -1 because we are reading the null character

def main():
    filename = 'file.txt'
    cloudsize = '4'
    test_input = filename + ' ' + cloudsize
    Weather(test_input)

if __name__ == '__main__':
    main()