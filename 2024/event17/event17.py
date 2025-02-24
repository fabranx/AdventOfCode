class Register:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.A = 0
            cls._instance.B = 0
            cls._instance.C = 0
        return cls._instance


def init_register(A, B, C):
    register = Register()
    register.A = A
    register.B = B
    register.C = C

def adv(combo):
    register = Register()
    numerator = register.A
    value = combo_operand(combo)
    if value is not None:
        denominator = 2**value
        result = numerator // denominator
        register.A = result
    return None


def bxl(value):
    register = Register()
    register.B = register.B ^ value
    return None


def bst(combo):
    register = Register()
    value = combo_operand(combo)
    if value is not None:
        register.B = value % 8
    return None



def jnz(value):
    register = Register()
    if register.A != 0:
        return value
    else:
        return None

def bxc(value):
    register = Register()
    register.B = register.B ^ register.C
    return None


def out(combo):
    register = Register()
    value = combo_operand(combo)
    if value is not None:
        OUTPUT.append(value % 8)

def bdv(combo):
    register = Register()
    numerator = register.A
    value = combo_operand(combo)
    if value is not None:
        denominator = 2 ** value
        result = numerator // denominator
        register.B = result
    return None

def cdv(combo):
    register = Register()
    numerator = register.A
    value = combo_operand(combo)
    if value is not None:
        denominator = 2 ** value
        result = numerator // denominator
        register.C = result
    return None

def combo_operand(combo):
    register = Register()
    if 0 <= combo <= 3:
        return combo
    elif combo == 4:
        return register.A
    elif combo == 5:
        return register.B
    elif combo == 6:
        return register.C
    else:
        return None


opcodes = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

OUTPUT = []

def main():
    with open('data.txt', 'r') as f:
        registers, program = f.read().split('\n\n')

    reg_A_val, reg_B_val, reg_C_val = registers.split('\n')
    reg_A_val = int(reg_A_val.split(':')[1])
    reg_B_val = int(reg_B_val.split(':')[1])
    reg_C_val = int(reg_C_val.split(':')[1])

    inst_vals = [int(val) for val in program.strip().split(':')[1].split(',')]

    ### PART ONE
    # init_register(reg_A_val, reg_B_val, reg_C_val)
    # pointer = 0
    # while pointer < len(inst_vals):
    #     opcode = inst_vals[pointer]
    #     if pointer+1 >= len(inst_vals):
    #         print("END OF INSTRUCTIONS")
    #         break
    #
    #     val = inst_vals[pointer+1]
    #     func = opcodes[opcode]
    #     ret = func(val)
    #     if ret is not None:
    #         pointer = ret
    #     else:
    #         pointer += 2
    #
    # print(','.join([f"{v}" for v in OUTPUT]))


    for i in range(1000000, 10000000):
        init_register(i, 0, 0)
        global OUTPUT
        OUTPUT = []
        pointer = 0
        while pointer < len(inst_vals):
            opcode = inst_vals[pointer]
            if pointer+1 >= len(inst_vals):
                print("END OF INSTRUCTIONS")
                break

            val = inst_vals[pointer+1]
            func = opcodes[opcode]
            ret = func(val)
            if ret is not None:
                pointer = ret
            else:
                pointer += 2

            if len(OUTPUT) > len(inst_vals):
                break

        if OUTPUT == inst_vals:
            print(i)

        # print(i, ','.join([f"{v}" for v in OUTPUT]))



if __name__ == '__main__':
    main()
