
MODULO = 16777216


def step1(secret_number):
    res = secret_number * 64
    secret_number = mix(res, secret_number)
    secret_number = prune(secret_number)
    return secret_number

def step2(secret_number):
    res = secret_number // 32
    secret_number = mix(res, secret_number)
    secret_number = prune(secret_number)
    return secret_number

def step3(secret_number):
    res = secret_number * 2048
    secret_number = mix(res, secret_number)
    secret_number = prune(secret_number)
    return secret_number

def prune(secret_number):
    new_secret_number = secret_number % MODULO
    return new_secret_number


def mix(number, secret_number):
    new_secret_number = number ^ secret_number
    return new_secret_number

def calculate(secret_number):
    secret_number = step1(secret_number)
    secret_number = step2(secret_number)
    secret_number = step3(secret_number)
    return secret_number

def main():
    with open('data.txt', 'r') as f:
        initial_secrets_numbers = [int(num) for num in f.read().split('\n')]

    print(initial_secrets_numbers)

    total = 0
    for secret_number in initial_secrets_numbers:
        isn = secret_number
        for _ in range(2000):
            secret_number = calculate(secret_number)

        print(f"{isn}: {secret_number}")
        total += secret_number

    print(total)

if __name__ == '__main__':
    main()
