
# Maze Problem

class Maze():
    def __init__(self):
        self.matrix = []
        self.col_size = 0
        self.row_size = 0

        self.readFile()    # Matrix should now be filled with list of lists and col and row size are initialized

        self.start = self.findStart()       # Tuple of Start Coord (row, col)

        # TESTING FOR NEXT POINT AND IN BOUNDS
        # print("start", self.start)
        # nextPoint = self.nextPoint(self.start, "west")
        # print("nextPoint", nextPoint)
        # if self.inBounds(nextPoint):
        #     print("nextpoint in bounds")
        # else:
        #     print("next point out of bounds")

        path = self.search(self.start)
        if not path:
            print("No Solution")
        else:
            print(path)

    # Open + Read File + Store
    def readFile(self):
        f = open("maze.txt", "r")

        if f.mode == 'r':
            contents = f.read()
            line = ""
            for char in contents:                   # Read through contents and store in lists of lists
                if (len(line) == 4):
                    self.matrix.append(line)
                    line = ""
                elif char.isalpha or char.isdigit:  # This lets it skip through spaces and newlines
                    line += char
                else:
                    print("here")
            print(self.matrix)

        self.col_size = len(self.matrix)
        self.row_size = len(self.matrix[0])

    # Returns Coordinate of Starting Point in (y,x) where y is row and x is column
    def findStart(self):
        for y in range(self.col_size):
            for x in range(self.row_size):
                # print(self.matrix[y][x])
                if self.matrix[y][x] == 'S':
                    return (y,x)

    def search(self, current):
        stack = []
        directions = ['north', 'south', 'west', 'east']

        # INITIALIZE THE STACK
        for direction in directions:
            nextPoint = self.nextPoint(current, direction)
            if self.inBounds(nextPoint):
                stack.append((nextPoint, [current], [direction]))             # stack.append( nextPoint, visited, path)

        while stack:
            stack_top = stack.pop()
            # print(stack_top)                                                      # testing purposes only
            if self.matrix[stack_top[0][0]][stack_top[0][1]] == "D":                # answer found
                return stack[-1][2]

            for direction in directions:
                nextPoint = self.nextPoint(stack_top[0], direction)

                if nextPoint not in stack_top[1]:                                   # checks if visited before
                    if self.inBounds(nextPoint):                                    # checks if in bounds
                        if self.matrix[stack_top[0][0]][stack_top[0][1]] == "1":    # checks if open
                            stack.append((nextPoint, stack_top[1] + [stack_top[0]], stack_top[2] + [direction]))

        return stack        # only reached if no solution exists. Returns an empty path

    def nextPoint(self, current, direction):
        if direction == "north":
            return (current[0] - 1, current[1])
        if direction == "west":
            return (current[0], current[1] - 1)
        if direction == "east":
            return (current[0], current[1] + 1)
        if direction == "south":
            return (current[0] + 1, current[1])
        else:
            print("Not direction")

    def inBounds(self, coord):
        if coord[0] < 0 or coord[0] >= self.col_size:
            return False
        if coord[1] < 0 or coord[1] >= self.row_size:
            return False
        return True


def main():
    maze = Maze()

if __name__ == "__main__":
    main()
