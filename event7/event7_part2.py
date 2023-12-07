# --- Part Two ---
#
# To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.
# To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.
# J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.
#
# Now, the above example goes very differently:
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
#
#     32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
#     KK677 is now the only two pair, making it the second-weakest hand.
#     T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
#
# With the new joker rule, the total winnings in this example are 5905.
# Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?


TYPES = {
    'FIVEKIND': 7,
    'FOURKIND': 6,
    'FULL': 5,
    'THREEKIND': 4,
    'TWOPAIR': 3,
    'ONEPAIR': 2,
    'HIGHCARD': 1
}

RANK = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}

SCHEMA = {
    (5,): 'FIVEKIND',
    (4, 1): 'FOURKIND',
    (3, 2): 'FULL',
    (3, 1, 1): 'THREEKIND',
    (2, 2, 1): 'TWOPAIR',
    (2, 1, 1, 1): 'ONEPAIR',
    (1, 1, 1, 1, 1): 'HIGHCARD',
}


def calculateTotalWinning(set_hands: list[tuple[str, int]]):
    handRanked = {}
    for hand in set_hands:
        print(hand)
        cards, bid = hand
        rank = getRank(cards)
        if rank not in handRanked:
            handRanked[rank] = [hand]  # create TYPE key and add hand in list value
        else:
            handRanked[rank].append(hand)   # add hand to list of his TYPE

    sortedKeys = sorted(handRanked.keys(), key=lambda x: TYPES[x])  # sort keys in handRanked by value of TYPE, from lowest to highest
    count = 0

    def sort(hand):
        """ sort all card in hand by his RANK from lowest to highest """
        values = []
        for label in hand[0]:
            values.append(RANK[label])
        return values

    moltiplicator = 1
    for key in sortedKeys:
        sortedHand = sorted(handRanked[key], key=sort)
        for hand in sortedHand:
            count = count + (moltiplicator * hand[1])
            moltiplicator += 1

    return count

def getRank(hand_cards: str):
    """ given cards in a hand, return type of hand (FULL, ONEPAIR, ...) and  """
    countRank = {}
    countJ = 0
    for card in hand_cards:  # insert in countRank all type of card except type J
        if card == 'J':
            countJ += 1
            continue
        if card not in countRank:
            countRank[card] = 1
        else:
            countRank[card] += 1

    if 0 < countJ < 5:  # at least on J or max J
        maxValue = 0
        maxKey = ''
        # print(countRank)
        for key, value in countRank.items():
            if value == maxValue:  # if same value consider the highest type card
                if RANK[key] > RANK[maxKey]:
                    # maxValue = value
                    maxKey = key
            if value > maxValue:  # update the type of card and the quantity in hand
                maxValue = value
                maxKey = key

        countRank[maxKey] += countJ   # add number of J in hand to the highest card with the max quantity, for make the hand the strongest type possible

    elif countJ == 5:
        countRank = {'J': 5}

    ranks = tuple(sorted(countRank.values(), reverse=True))
    return SCHEMA[ranks]


if __name__ == '__main__':
    with open('inputData.txt', 'r') as file:
        lines = []
        for line in file.readlines():
            lines.append(line.strip())

    hands = []
    for line in lines:
        card, bid = line.split()
        hands.append((card, int(bid)))

    print(calculateTotalWinning(hands))

    # hands = [
    #     ("32T3K", 765),
    #     ("T55J5", 684),
    #     ("KK677", 28),
    #     ("KTJJT", 220),
    #     ("QQQJA", 483),
    # ]
    # print(calculateTotalWinning(hands))
