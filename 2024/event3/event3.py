# https://adventofcode.com/2024/day/3

import re

def main():
    with open('data.txt', 'r') as f:
        string = f.read().strip()

    # PART ONE
    pattern = r"mul\((\d+),(\d+)\)"
    results = re.findall(pattern, string)
    sum = 0
    for res in results:
        sum += int(res[0]) * int(res[1])

    print(sum)


    # PART TWO
    pattern_do_dont = r"(?:do\(\)|^)(.*?)(?:don't\(\)|$)"
    do_dont_str = re.findall(pattern_do_dont, string, re.DOTALL)
    # print(do_dont_str)
    string = ''.join(do_dont_str)
    results = re.findall(pattern, string)

    # print(results)
    sum = 0
    for res in results:
        sum += int(res[0]) * int(res[1])

    print(sum)


if __name__ == '__main__':
    main()