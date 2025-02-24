# https://adventofcode.com/2024/day/2

def correctly_increase(report):
    for i in range(len(report) - 1):
        if report[i] > report[i + 1] or not (1 <= report[i + 1] - report[i] <= 3):
            return False
    return True


def correctly_decrease(report):
    for i in range(len(report) - 1):
        if report[i] < report[i + 1] or not (1 <= report[i] - report[i + 1] <= 3):
            return False
    return True


def correctly_increase_dampener(report):
    for i in range(len(report) - 1):
        if report[i] > report[i + 1] or not (1 <= report[i + 1] - report[i] <= 3):
            if (i + 2) < len(report):
                if report[i] > report[i + 2] or not (1 <= report[i + 2] - report[i] <= 3):
                    return False
    return True


def correctly_decrease_dampener(report):
    for i in range(len(report) - 1):
        if report[i] < report[i + 1] or not (1 <= report[i] - report[i + 1] <= 3):
            if i + 2 < len(report):
                if report[i] > report[i + 2] or not (1 <= report[i + 2] - report[i] <= 3):
                    return False

    return True


def main():
    with open('data.txt', 'r') as f:
        reports = [[int(num) for num in line.split()] for line in f.readlines()]

    safe_reports = 0
    safe_dampener_reports = 0
    for report in reports:
        if report[0] > report[1]:
            if correctly_decrease(report):
                safe_reports += 1
            if correctly_decrease_dampener(report):
                print(report)
                safe_dampener_reports += 1
        elif report[0] < report[1]:
            if correctly_increase(report):
                safe_reports += 1
            if correctly_increase_dampener(report):
                print(report)
                safe_dampener_reports += 1

    print(safe_reports)  # PART ONE
    print(safe_dampener_reports) # PART TWO


if __name__ == '__main__':
    main()
