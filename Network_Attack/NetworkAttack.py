
nodeDict = dict()

def DFS(dict):
    max_attack = 0
    visited = []
    stack = []

    for key in nodeDict.keys():
        current_node = dict[key]
        if current_node.val not in visited:
            stack.append(current_node)

            current_attack = 0
            while stack:
                stack_node = stack.pop()
                if stack_node.val not in visited:
                    visited.append(stack_node.val)
                    current_attack += 1
                    for neighbor in stack_node.neighbors:
                        stack.append(dict[int(neighbor)])
            if current_attack > max_attack:
                max_attack = current_attack

    return max_attack

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

filename = input('Here')

f = open(filename, 'r')

line = f.readline()
if '\0' in line:
    line = line[:-1]

case_count = 1
while True:
    n = int(line)
    # print(n)
    if n == 0:
         break
    for i in range(n):
        line = f.readline()
        line = line[:-1]
        num_neighbors = line[0]
        neighbors = line[1:].split()
        new_node = Node(i, neighbors)
        nodeDict[i] = new_node

    # DFS
    max_attack = DFS(nodeDict)
    print(f'Case {case_count}: ', max_attack)
    case_count += 1

    for key in nodeDict.keys():
        print(f'key: {key}, node: {nodeDict[key].neighbors}')
    nodeDict = dict()


    line = f.readline()





