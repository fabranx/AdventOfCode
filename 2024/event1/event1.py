# https://adventofcode.com/2024/day/1

def main():
    with open('data.txt', 'r') as f:
        rows = [line.strip() for line in f.readlines()]

        left_col = sorted([int(row.split()[0]) for row in rows])
        right_col = sorted([int(row.split()[1]) for row in rows])

    ### PART ONE
    sum = 0
    for i in range(len(rows)):
        sum += abs(left_col[i] - right_col[i])
    print(sum)

    ### PART TWO
    count_sum = 0
    for num in left_col:
        count_sum += right_col.count(num) * num

    print(count_sum)


if __name__ == '__main__':
    main()
