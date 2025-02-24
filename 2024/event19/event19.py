from itertools import combinations, permutations, combinations_with_replacement, product
from functools import cache

def solve(word, patterns):
    if len(word) == 0:
        return True
    isValid = False
    for pattern in patterns:
        if word.startswith(pattern):
            res = solve(word[len(pattern):], patterns)
            if res:
                isValid = True
                break
    return isValid



def main():
    with open('data.txt', 'r') as f:
        patterns, designs = f.read().strip().split('\n\n')
        patterns = [pattern.strip() for pattern in patterns.strip().split(',')]
        designs = designs.split('\n')
        print(patterns)
        print(designs)

    patterns = sorted(patterns, key=lambda v: len(v), reverse=True)

    count = 0
    for design in designs:
        res = solve(design, patterns)
        if res:
            count += 1
        print(design, res)

    print(count)
    # valid, not_valid = checkPossibleDesign(designs, patterns)




if __name__ == '__main__':
    main()
