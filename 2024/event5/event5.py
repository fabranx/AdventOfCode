def main():
    with open('data.txt', 'r') as f:
        splitted = f.read().split('\n')
        sep_index = splitted.index('')
        rules = splitted[:sep_index]
        updates = splitted[sep_index+1:]

        print(rules)
        print(updates)

    number_rules = {}
    for rule in rules:
        before, after = rule.split('|')
        if before in number_rules:
            number_rules[before].append(after)
        else:
            number_rules[before] = [after]

    print(number_rules)

    corrected_rules = []

    for update in updates:
        update = update.split(',')
        len_update = len(update)
        isCorrected = True
        for i in range(len_update):
            bef = update[i]
            for j in range(i+1, len_update):
                aft = update[j]
                if bef in number_rules:
                    if aft not in number_rules[bef]:
                        isCorrected = False
                        break
                else:
                    continue
            if not isCorrected:
                break

        if isCorrected:
            corrected_rules.append(update)

    print(corrected_rules)

    for rule in corrected_rules:
        for i in reversed(range(len(rule))):
            aft = rule[i]
            for j in reversed(range(i)):
                bef = rule[j]
                print(aft, bef)
                if aft in number_rules:
                    if bef not in number_rules[aft]:
                        continue
                    else:
                        corrected_rules.remove(rule)
                        break

    print(corrected_rules)
    sum = 0
    for rule in corrected_rules:
        mid = (len(rule) // 2)
        print(mid, rule[mid])
        sum += int(rule[mid])

    print(sum)











if __name__ == '__main__':
    main()