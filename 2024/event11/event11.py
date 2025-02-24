N_BLINKING = 75
def calculate_stones(el, blink=0, memo=None):
    # print(f"{el} -> {blink}")
    # print(blink)
    if memo is None:
        memo = {}
    if blink >= N_BLINKING:
        return 1

    if (el, blink) in memo:
        return memo[(el, blink)]

    final_stones = []
    if el == 0:
        final_stones.append(1)
    elif len(str(el)) % 2 == 0:
        n = str(el)
        left_half = int(n[:len(n) // 2])
        right_half = int(n[len(n) // 2:])
        final_stones.append(left_half)
        final_stones.append(right_half)
    else:
        final_stones.append(el * 2024)
    # if blink == N_BLINKING:
    #     return len(final_stones)
    count = 0
    for el in final_stones:
        memo[(el, blink+1)] = calculate_stones(el, blink+1, memo)
        count += memo[(el, blink+1)]
    return count


def main():
    with open('data.txt', 'r') as f:
        stones = f.readline().strip().split()
        print(stones)

    stones = [int(val) for val in stones]
    print(stones)
    # for i in range(N_BLINKING):
    #     print(i)
    #     new_stones = []
    #     for ch in stones:
    #         if ch == 0:
    #             new_stones.append(1)
    #         elif len(str(ch)) % 2 == 0:
    #             n = str(ch)
    #             left_half = int(n[:len(n)//2])
    #             right_half = int(n[len(n)//2:])
    #             new_stones.append(left_half)
    #             new_stones.append(right_half)
    #         else:
    #             new_stones.append(ch*2024)
    #
    #     stones = new_stones
    #
    # print(len(stones))

    count = 0
    for c, ch in enumerate(stones):
        print(ch)
        count += calculate_stones(ch)
        # new_stones = [ch]
        # for i in range(N_BLINKING):
        #     print(f"{c}/{len(stones)} -> BLINK {i}")
        #     final_stones = []
        #     for el in new_stones:
        #         if el == 0:
        #             final_stones.append(1)
        #         elif len(str(el)) % 2 == 0:
        #             n = str(el)
        #             left_half = int(n[:len(n)//2])
        #             right_half = int(n[len(n)//2:])
        #             final_stones.append(left_half)
        #             final_stones.append(right_half)
        #         else:
        #             final_stones.append(el*2024)
        #     new_stones = final_stones
        # count += len(new_stones)

    print(count)


if __name__ == '__main__':
    main()
