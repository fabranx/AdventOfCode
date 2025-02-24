def diskMapToBlock(diskMap: str):
    block = []
    id_ = 0
    for i, value in enumerate(diskMap):
        if i % 2 == 0:  # is a file
            for _ in range(int(value)):
                block.append(str(id_))
            # block.append(str(id_) * int(value))
            id_ += 1
        else:  # is a free space
            for _ in range(int(value)):
                block.append('.')
            # block.append('.' * int(value))

    return block

def compact(block):
    free_space = [(pos, space) for pos, space in enumerate(block) if space == '.']
    files = list(reversed([(pos, file) for pos, file in enumerate(block) if '.' not in file]))

    print(free_space)
    print(files)

    for i, space in enumerate(free_space):
        space_pos = space[0]
        space_val = space[1]
        file_pos = files[i][0]
        file_val = files[i][1]

        if space_pos < file_pos:
            block[space_pos] = file_val
            block[file_pos] = space_val

    return block



def diskMapToBlock2(diskMap: str):
    block = []
    id_ = 0
    index_pos = 0
    for i, value in enumerate(diskMap):
        if i % 2 == 0:  # is a file
            if int(value != 0):
                block.append((str(id_), str(id_) * int(value), index_pos))
            id_ += 1
            index_pos += int(value)
        else:  # is a free space
            if int(value) != 0:
                block.append(('.', '.' * int(value), index_pos))
            index_pos += int(value)


    return block


def searchFreeSpace(length: int, block: list[str]):
    # print(block)
    count = 0
    pos = None
    for i, ch in enumerate(block):
        if ch == '.':
            if count == 0:
                pos = i
            count += 1
        else:
            count = 0
        if count == length:
            return pos
    # return block.find('.'*length)


def aggregate(block, aggr_block):
    free_space = []
    files = []
    print(aggr_block)
    for val in block:
        if val[0] == '.':
            free_space.append(val)
        else:
            files.append(val)
    # print(free_space)
    # print(files)

    for i, file in enumerate(reversed(files)):
        id_ = file[0]
        file_str = file[1]
        initial_pos = file[2]
        length = file_str.count(id_)
        pos = searchFreeSpace(length, aggr_block)
        if 0 < pos < initial_pos:
            for j in range(length):
                aggr_block[pos+j] = id_
                aggr_block[initial_pos+j] = '.'

    return aggr_block



def main():
    with open('data.txt', 'r') as f:
        disk_map = f.read().strip()
        print(disk_map)

        #### PART ONE
        # block = diskMapToBlock(disk_map)
        # print(block)
        # compacted = compact(block)
        # print(''.join(compacted))
        # result = 0
        # for i, value in enumerate(compacted):
        #     if value == '.':
        #         continue
        #     result += int(i) * int(value)
        #
        # print(result)



        #### PART TWO
        block = diskMapToBlock2(disk_map)
        # print(block)
        aggregate_block = aggregate(block, diskMapToBlock(disk_map))
        print(*aggregate_block)
        result = 0
        for i, value in enumerate(aggregate_block):
            if value == '.':
                continue
            result += int(i) * int(value)

        print(result)


if __name__ == '__main__':
    main()
