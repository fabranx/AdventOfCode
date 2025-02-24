def find_start_end(race_track):
    start = None
    end = None
    for i, row in enumerate(race_track):
        if 'S' in row:
            start = (i, row.index('S'))
        elif 'E' in row:
            end = (i, row.index('E'))
        if start is not None and end is not None:
            break
    return start, end



def path(race_track):
    start, end = find_start_end(race_track)
    pos = start
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    path_ = [start]
    while pos != end:
        for direction in directions:
            next_pos = (pos[0]+direction[0], pos[1]+direction[1])
            if 0 <= next_pos[0] < len(race_track) and 0 <= next_pos[1] < len(race_track[next_pos[0]]):
                next_ch = race_track[next_pos[0]][next_pos[1]]
                if next_pos not in path_ and (next_ch == '.' or next_ch == 'E'):
                    path_.append((next_pos[0], next_pos[1]))
                    pos = next_pos
                    break

    return path_


def find_cheats(race_track, path_):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cheats = []
    saved = {}
    for pos in path_:
        for direction in directions:
            next_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if 0 <= next_pos[0] < len(race_track) and 0 <= next_pos[1] < len(race_track[next_pos[0]]):
                next_ch = race_track[next_pos[0]][next_pos[1]]
                if next_ch == '#':
                    next2_pos = (next_pos[0]+direction[0], next_pos[1]+direction[1])
                    if 0 <= next2_pos[0] < len(race_track) and 0 <= next2_pos[1] < len(race_track[next2_pos[0]]):
                        next2_ch = race_track[next2_pos[0]][next2_pos[1]]
                        if (next2_ch == '.' or next2_ch == 'E') and next2_pos in path_:
                            pos_index = path_.index(pos)
                            next2_index = path_.index(next2_pos)
                            if pos_index < next2_index:
                                # print(f"saved {next2_index-pos_index -2}")
                                s = next2_index-pos_index - 2
                                if s in saved:
                                    saved[s] = saved[s] + 1
                                else:
                                    saved[s] = 1
                                cheat = path_[:pos_index]
                                cheat.append(next_pos)
                                cheat.append(path_[next2_index:])
                                cheats.append(cheat)
                                # cheats.append([ch for i, ch in enumerate(path_) if 0 <= i <= pos_index or next2_index <= i <= len(path_)])
    return cheats, saved


def main():
    with open('data.txt', 'r') as f:
        race_track = [[ch for ch in row.strip()] for row in f.readlines()]

        print(race_track)

        path_ = path(race_track)
        # print(path_)
        print(len(path_))

        cheats_path, ps_saved = find_cheats(race_track, path_)
        # print(cheats_path)
        print(len(cheats_path))
        print(ps_saved)

        maj_100 = 0
        for time in ps_saved.keys():
            if time >= 100:
                maj_100 += ps_saved[time]

        print(maj_100)







if __name__ == '__main__':
    main()
