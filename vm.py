


stack = []
new_name = ''

while new_name != 'quit':
    new_name = input('Enter virtual machine commands:')
    command = new_name[0]

    if command == 'P':
        stack.append(int(new_name[2:]))
    if command == 'A':
        if len(stack) < 2:
            print('Not enough values in stack')
        else:
            first = stack.pop()
            second = stack.pop()
            result = first + second
            stack.append(result)

    if command == 'M':
        if len(stack) < 2:
            print('Not enough values in stack')
        else:
            first = stack.pop()
            second = stack.pop()
            result = first * second
            stack.append(result)
    if command == 'S':
        if len(stack) < 2:
            print('Not enough values in stack')
        else:
            first = stack.pop()
            second = stack.pop()
            result = second - first
            stack.append(result)
    if command == 'D':
        if len(stack) < 2:
            print('Not enough values in stack')
        else:
            first = stack.pop()
            second = stack.pop()
            result = second/first
            stack.append(result)
    if command == 'R':
        print('=> ' , stack[-1])

    print(stack)





