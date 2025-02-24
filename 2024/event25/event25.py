def getKeyPinHeight(key):
    pin_height = []
    for col in range(len(key[0])):
        pin = []
        for row in range(len(key)-1):
            pin.append(key[row][col])
        pin_height.append(pin.count('#'))

    return tuple(pin_height)


def getLockPinHeight(lock):
    lock_height = []
    for col in range(len(lock[0])):
        pin = []
        for row in range(1, len(lock)):
            pin.append(lock[row][col])
        lock_height.append(pin.count('#'))

    return tuple(lock_height)

def check_fit(lock_h, key_h):
    MAX_PIN_H = 5
    for i in range(len(lock_h)):
        if key_h[i] > (MAX_PIN_H - lock_h[i]):
            return False
    return True


def main():
    with open('data.txt', 'r') as f:
        schematics = []
        for schema_str in f.read().split('\n\n'):
            schema = []
            for row in schema_str.split('\n'):
                schema.append(row)
            schematics.append(schema)

    print(len(schematics))

    keys = []
    locks = []
    for schema in schematics:
        if schema[0] == "#####":
            locks.append(schema)
        elif schema[-1] == '#####':
            keys.append(schema)
        else:
            print("ERROR")

    print(len(keys))
    print(len(locks))

    keys_height = []
    for key in keys:
        pin = getKeyPinHeight(key)
        # print(pin)
        keys_height.append(pin)

    locks_height = []
    for lock in locks:
        pin = getLockPinHeight(lock)
        # print(pin)
        locks_height.append(pin)

    MAX_PIN_H = 5
    c_valid = 0
    for lock_h in locks_height:
        for key_h in keys_height:
            if check_fit(lock_h, key_h):
                c_valid += 1

    print(c_valid)


if __name__ == '__main__':
    main()

