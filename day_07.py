from collections import Counter

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
    "2": 2
}

CARD_VALUE_WITH_JOKERS_WILD = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


def five_of_a_kind(cards):
    return len(cards) == 5 and len(set(cards)) == 1

def four_of_a_kind(cards):
    card_counter = Counter(cards)
    two_most_common = card_counter.most_common(2)
    return len(cards) == 5 and len(two_most_common) >= 2 and two_most_common[0][1] == 4 and  two_most_common[1][1] == 1

def full_house(cards):
    card_counter = Counter(cards)
    two_most_common = card_counter.most_common(2)
    return len(cards) == 5 and len(two_most_common) == 2 and two_most_common[0][1] == 3 and two_most_common[1][1] == 2

def three_of_a_kind(cards):
    card_counter = Counter(cards)
    two_most_common = card_counter.most_common(2)
    return len(cards) == 5 and len(two_most_common) == 2 and two_most_common[0][1] == 3 and two_most_common[1][1] == 1

def two_pair(cards):
    card_counter = Counter(cards)
    two_most_common = card_counter.most_common(2)
    return len(cards) == 5 and len(two_most_common) == 2 and two_most_common[0][1] == 2 and two_most_common[1][1] == 2

def one_pair(cards):
    card_counter = Counter(cards)
    two_most_common = card_counter.most_common(2)
    return len(cards) == 5 and len(two_most_common) == 2 and two_most_common[0][1] == 2 and two_most_common[1][1] == 1

def high_card(cards):
    card_counter = Counter(cards)
    most_common = card_counter.most_common(1)
    return len(cards) == 5 and most_common[0][1] == 1

class CamelCardHand:
    def __init__(self, cards, bid=0):
        self.cards = cards
        self.bid = bid

    @classmethod
    def from_line(cls, line):
        return cls(line[:5], int(line[6:]))

    def _five_of_a_kind(self):
        return five_of_a_kind(self.cards)

    def _four_of_a_kind(self):
        return four_of_a_kind(self.cards)

    def _full_house(self):
        return full_house(self.cards)

    def _three_of_a_kind(self):
        return three_of_a_kind(self.cards)
    def _two_pair(self):
       return two_pair(self.cards)

    def _one_pair(self):
       return one_pair(self.cards)

    def  _high_card(self):
        return high_card(self.cards)

    def get_rank(self):
        if self._five_of_a_kind():
            return 7
        elif self._four_of_a_kind():
            return 6
        elif self._full_house():
            return 5
        elif self._three_of_a_kind():
            return 4
        elif self._two_pair():
            return 3
        elif self._one_pair():
            return 2
        elif self._high_card():
            return 1
        else:
            return 0

    def __lt__(self, other):
        self_rank = self.get_rank()
        other_rank = other.get_rank()

        if self_rank == other_rank:
            self_card_values = [CARD_VALUE[c] for c in self.cards]
            other_card_values = [CARD_VALUE[c] for c in other.cards]
            return self_card_values < other_card_values
        else:
            return self_rank < other_rank


    def __eq__(self, other):
        self_rank = self.get_rank()
        other_rank = other.get_rank()
        if self_rank == other_rank:
            self_card_values = [CARD_VALUE[c] for c in self.cards]
            other_card_values = [CARD_VALUE[c] for c in other.cards]
            return self_card_values  == other_card_values
        else:
            False

class CamelCardsHandJokerWild():
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.best_cards = self._get_best_cards()


    @classmethod
    def from_line(cls, line):
        return cls(line[:5], int(line[6:]))

    def _get_best_cards(self):
        if "J" not in self.cards:
            return self.cards

        possible_hands = [CamelCardHand(self.cards.replace("J", card)) for card in CARD_VALUE.keys()]
        sorted_hands = sorted(possible_hands, reverse=True)
        return sorted_hands[0].cards

    def get_rank(self):
        if five_of_a_kind(self.best_cards):
            return 7
        elif four_of_a_kind(self.best_cards):
            return 6
        elif full_house(self.best_cards):
            return 5
        elif three_of_a_kind(self.best_cards):
            return 4
        elif two_pair(self.best_cards):
            return 3
        elif one_pair(self.best_cards):
            return 2
        elif high_card(self.best_cards):
            return 1
        else:
            return 0

    def __lt__(self, other):
        self_rank = self.get_rank()
        other_rank = other.get_rank()

        if self_rank == other_rank:
            self_card_values = [CARD_VALUE_WITH_JOKERS_WILD[c] for c in self.cards]
            other_card_values = [CARD_VALUE_WITH_JOKERS_WILD[c] for c in other.cards]
            return self_card_values < other_card_values
        else:
            return self_rank < other_rank


    def __eq__(self, other):
        self_rank = self.get_rank()
        other_rank = other.get_rank()
        if self_rank == other_rank:
            self_card_values = [CARD_VALUE_WITH_JOKERS_WILD[c] for c in self.cards]
            other_card_values = [CARD_VALUE_WITH_JOKERS_WILD[c] for c in other.cards]
            return self_card_values  == other_card_values
        else:
            False




if __name__ == '__main__':

    with open('data/day_07_input.txt') as f:
        lines = f.readlines()
    #
    # with open('data/day_07_example.txt') as f:
    #     lines = f.readlines()

    hands = [CamelCardHand.from_line(line.strip()) for line in lines]

    sorted_hands = sorted(hands)

    sum_of_values = sum([(i+1) * hand.bid for i, hand in enumerate(sorted_hands)])

    print(f"Part 1: {sum_of_values}")

    hands_w_jokers = [CamelCardsHandJokerWild.from_line(line.strip()) for line in lines]
    sorted_hands_w_jokers  = sorted(hands_w_jokers)

    sum_of_values_part_2 = sum([(i + 1) * hand.bid for i, hand in enumerate(sorted_hands_w_jokers)])
    print(f"Part 2: {sum_of_values_part_2}")