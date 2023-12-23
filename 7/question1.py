from enum import Enum


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


CARD_VALUE = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

        if len(self.hand) != 5:
            raise TypeError("Bad card count in hand: " + hand)

        # Parse hand
        counts = {}
        highest = 0
        for card in hand:
            if card not in counts:
                counts[card] = 1
            else:
                counts[card] += 1
            highest = counts[card] if counts[card] > highest else highest

        match highest:
            case 5:
                self.type = HandType.FIVE_OF_A_KIND
            case 4:
                self.type = HandType.FOUR_OF_A_KIND
            case 3:
                self.type = HandType.THREE_OF_A_KIND
                for v in counts.values():
                    if v == 2:
                        self.type = HandType.FULL_HOUSE
                        break
            case 2:
                pair_count = 0
                for v in counts.values():
                    if v == 2:
                        pair_count += 1
                if pair_count == 2:
                    self.type = HandType.TWO_PAIR
                else:
                    self.type = HandType.ONE_PAIR
            case 1:
                self.type = HandType.HIGH_CARD

    def __lt__(self, other):
        if self.type != other.type:
            return self.type.value < other.type.value
        else:
            for i in range(0, len(self.hand)):
                if self.hand[i] != other.hand[i]:
                    return CARD_VALUE[self.hand[i]] < CARD_VALUE[other.hand[i]]
            return True

    def __gt__(self, other):
        if self.type != other.type:
            return self.type.value > other.type.value
        else:
            for i in range(0, len(self.hand)):
                if self.hand[i] != other.hand[i]:
                    return CARD_VALUE[self.hand[i]] > CARD_VALUE[other.hand[i]]
            return True

    def __str__(self):
        return (
            "Cards: '"
            + self.hand
            + "' - Bid: "
            + str(self.bid)
            + " - Type: "
            + self.type.name
        )


games = []
with open("puzzle-input.txt") as file:
    for line in file:
        entries = line.strip().split()
        games.append(Hand(entries[0], int(entries[1])))

games = sorted(games)

sum = 0
rank = 1
for game in games:
    sum += game.bid * rank
    rank += 1
print(sum)
