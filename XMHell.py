# Competive Programming XMHell

# Shravani Badadha and Kit Ha
# 3/5/2020

stack = []

filename = input()
f = open(filename, 'r+')

line = f.read()

for index in range(len(line)):
    if line[index] == '<':
        for second_index in range(index + 1, len(line)):
            if line[second_index] == '>':
                tag = line[index:second_index + 1]

                if stack:
                    # print(f'stack top: {stack[-1][1:]}, tag: {tag[2:]}')
                    if tag[2:] == stack[-1][1:]:
                        stack.pop()
                    else:
                        stack.append(tag)
                else:
                    stack.append(tag)

                index = second_index
                print(f'current stack: {stack}')
                break

if stack:
    print('invalid')
    print('invalid stack:', stack)
else:
    print('valid')