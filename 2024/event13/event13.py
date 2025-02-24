from sympy import symbols, solve



def main():
    with open('data.txt', 'r') as f:
        data = [claw_machine for claw_machine in f.read().split('\n\n')]
        print(data)


    costA = 3
    costB = 1
    totalTokens = 0
    partTwoDeltaPos = 10000000000000
    for row in data:
        row = row.split('\n')
        A = row[0].split(':')[1].split(',')
        B = row[1].split(':')[1].split(',')
        Prize = row[2].split(':')[1].split(',')

        Ax = int(A[0].strip().replace('X+', ''))
        Ay = int(A[1].strip().replace('Y+', ''))
        Bx = int(B[0].strip().replace('X+', ''))
        By = int(B[1].strip().replace('Y+', ''))
        ### PART ONE
        PrizeX = int(Prize[0].strip().replace('X=', ''))
        PrizeY = int(Prize[1].strip().replace('Y=', ''))
        ### PART TWO
        PrizeX = int(Prize[0].strip().replace('X=', '')) + partTwoDeltaPos
        PrizeY = int(Prize[1].strip().replace('Y=', '')) + partTwoDeltaPos

        # print(f"A: {Ax}-{Ay}\nB: {Bx}-{By}\nPrize: {PrizeX}-{PrizeY}")

        a, b = symbols('a b', integer=True)
        eq1 = Ax * a + Bx * b - PrizeX
        eq2 = Ay * a + By * b - PrizeY

        sol = solve((eq1, eq2), (a, b))

        if sol:
            tokenA = costA * sol[a]
            tokenB = costB * sol[b]
            totalTokens += tokenA+tokenB
            print(f"{PrizeX},{PrizeY} = A:{sol[a]} ; B{sol[b]} -> Token: {tokenA+tokenB}")
        else:
            print(f"{PrizeX},{PrizeY} = No soluzioni")
    print(totalTokens)

if __name__ == '__main__':
    main()
