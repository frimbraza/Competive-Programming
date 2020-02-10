# Kit Ha
# String Chain
input = "carpenter thread ratchet dummy sally yes yellow dat world"

class Node():
    def __init__(self, name, connections):
        self.val = name
        self.connect = connections

    def __str__(self):
        return f"val: {self.val}, connect: {self.connect}"

def GenerateNode(name, connections):
    final = []
    for connection in connections:
        if connection[0] == name[-1]:
            final.append(connection)
    # print(f"final: {final}")
    return Node(name, final)

def Solve(NodeList, target):
    for node in NodeList:
        stack = []
        for connect in node.connect:
            stack.append((connect, [node.val]))         # the next word, [of prev words]

        # print("stack:",stack)

        while stack:
            current_stack_item = stack.pop()
            new_path = current_stack_item[1] + [current_stack_item[0]]
            if len(new_path) == target:
                return new_path

            new_connects = []
            for node in NodeList:
                if node.val == current_stack_item[0]:
                    new_connects = node.connect

            new_connects = [connection for connection in new_connects if connection not in current_stack_item[1]]

            for connect in new_connects:
                # print("connect:", connect)
                # print("new_path", new_path)
                stack.append((connect, new_path))

    return ["Impossible"]

def split_words(words):
    return words.split()

def print_answer(answer):
    if answer == ["Impossible"]:
        return "Impossible"
    else:
        to_print = ""
        for word in answer[:-1]:
            word = word[:-1]
            word = word.capitalize()
            to_print += word

        to_print += answer[-1].capitalize()
        print(to_print)

if __name__ == "__main__":
    words = split_words(input)
    # print(words)

    nodeList = []
    for name in words:
        connections = [word for word in words if word != name]
        # print(f"name:{name}, connections:{connections}")
        nodeList.append(GenerateNode(name, connections))
        # print(f"name: {name}, connections: {connections}")

    answer = Solve(nodeList, len(words))
    print_answer(answer)