# https://adventofcode.com/2024/day/7

import itertools



def generate_combinations(nums, operations):
    comb_op = itertools.product(operations, repeat=len(nums) - 1)

    risultati = []

    for comb in comb_op:
        risultati.append(comb)

    return risultati

def main():
    with open('data.txt', 'r') as f:
        str_equations = [equation.strip() for equation in f.readlines()]


    equations = []
    for equation in str_equations:
        test_value, numbers = equation.split(':')
        equations.append((int(test_value), [int(num) for num in numbers.split()]))


    valids = []
    ### PART ONE
    operations = ['+', '*']
    for equation in equations:
        n_operations = len(equation[1])-1
        test_value = equation[0]
        numbers = equation[1]
        combinations = generate_combinations(numbers, operations)
        # print(combinations)
        for comb in combinations:
            res = 0
            if comb[0] == '+':
                res += numbers[0] + numbers[1]
            else:
                res += numbers[0] * numbers[1]
            for i in range(1, n_operations):
                if comb[i] == '+':
                    res += numbers[i+1]
                else:
                    res *= numbers[i+1]
            # print(res)
            if res == test_value:
                valids.append(test_value)
                break
    total = sum(valids)
    print(total)

    ## PART TWO
    valids = []
    operations = ['+', '*', '||']
    for equation in equations:
        n_operations = len(equation[1])-1
        test_value = equation[0]
        # print(test_value)
        numbers = equation[1]
        combinations = generate_combinations(numbers, operations)
        # print(combinations)
        for comb in combinations:
            res = 0
            if comb[0] == '+':
                res += numbers[0] + numbers[1]
            elif comb[0] == '*':
                res += numbers[0] * numbers[1]
            else:
                res = int(str(numbers[0]) + str(numbers[1]))
            for i in range(1, n_operations):
                if comb[i] == '+':
                    res += numbers[i+1]
                elif comb[i] == '*':
                    res *= numbers[i+1]
                else:
                    res = int(str(res) + str(numbers[i+1]))
            # print(res)
            if res == test_value:
                valids.append(test_value)
                break
    # print(valids)
    total = sum(valids)
    print(total)


if __name__ == '__main__':
    main()

