def main():
    with open('data.txt', 'r') as f:
        gates, operations = f.read().split('\n\n')
        # print(gates.split('\n'))
    gates = [gate.split(':') for gate in gates.split('\n')]
    gates = [(name, value) for name, value in gates]

    values = {}
    for name, value in gates:
        values[name] = int(value)

    print(values)
    print(gates)
    operations = [tuple(operation.replace(' -> ', ' ').split(' ')) for operation in operations.split('\n')]

    print(operations)

    for n1, op, n2, out in operations:
        if n1 in values and n2 in values:
            res = None
            print(op)
            if op == 'AND':
                res = values[n1] and values[n2]
            elif op == 'OR':
                res = values[n1] or values[n2]
            elif op == 'XOR':
                res = values[n1] ^ values[n2]
            values[out] = res
        else:
            operations.append((n1, op, n2, out))
            continue

    results = reversed(sorted([(name, value) for name, value in values.items() if not name.startswith('x') and not name.startswith('y')]))

    combined_bits = ''
    for name, value in results:
        if name.startswith('z'):
            combined_bits += str(value)

    print(combined_bits)
    print(int(combined_bits, 2))

if __name__ == '__main__':
    main()