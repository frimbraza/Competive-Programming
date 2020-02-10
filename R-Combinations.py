
# Remove itertools for more of a challenge
from itertools import combinations_with_replacement

r = 4
n = 4

def RCombo(ran, num_size):
    # generate
    output = generate(ran, num_size)
    num_combos = len(output)
    # for item in full_list:
    #     output.append(item)
    #     num_combos += 1
    #     if not output:
    #         output.append(item)
    #         num_combos += 1
    #     else:
    #         shouldAdd = True
    #         for number in output:
    #             if theSame(number, output):
    #                 shouldAdd = False
    #         if shouldAdd:
    #             output.append(item)
    #             num_combos += 1

    print("num of combos:", num_combos)
    printAnswer(output)

def generate(ran, num_size):
    combos = []
    for item in combinations_with_replacement(range(1,ran+1), num_size):
        combos.append([*item])
    return combos

def theSame(num1, num2): # list of numbers
    return count(num1) == count(num2)

def count(num):
    num_count = dict()
    for i in range(r + 1):
        for val in num:
            if val == i:
                # print(val)
                if val not in num_count.keys():
                    num_count[val] = 1
                else:
                    num_count[i] += 1

    return num_count

def printAnswer(answers):
    for answer in answers:
        line = ""
        for num in answer:
            line += str(num)
        print(line)

if __name__ == "__main__":
    RCombo(r,n)
