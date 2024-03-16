from collections import Counter
from dataclasses import dataclass

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

card_value_order = dict(zip('FEDCB98765432', range(0, 13)))


@dataclass(frozen=True)
class Hand:
    cards: str
    bid: int
    value: str


hands = set()
sorted_hands = set()


def find_value(counted_cards) -> str:
    five_of_a_kind = [5]
    five_of_a_kind.sort()

    four_of_a_kind = [4, 1]
    four_of_a_kind.sort()

    full_house = [3, 2]
    full_house.sort()

    three_of_a_kind = [3, 1, 1]
    three_of_a_kind.sort()

    two_pairs = [2, 2, 1]
    two_pairs.sort()

    one_pair = [2, 1, 1, 1]
    one_pair.sort()

    high_card = [1, 1, 1, 1, 1]
    high_card.sort()

    sorted_counted_cards = list(counted_cards.values())
    sorted_counted_cards.sort()
    if sorted_counted_cards == five_of_a_kind:
        return "7_five_of_a_kind"
    if sorted_counted_cards == four_of_a_kind:
        return "6_four_of_a_kind"
    if sorted_counted_cards == full_house:
        return "5_full_house"
    if sorted_counted_cards == three_of_a_kind:
        return "4_three_of_a_kind"
    if sorted_counted_cards == two_pairs:
        return "3_two_pairs"
    if sorted_counted_cards == one_pair:
        return "2_one_pair"
    if sorted_counted_cards == high_card:
        return "1_high_card"


def replace_for_sorting(cards_letter):
    return cards_letter.replace("T", "B").replace("J", "C").replace("Q", "D").replace("K", "E").replace("A", "F")


for line in all_lines:
    line = line.strip().split()
    line[0] = replace_for_sorting(line[0])
    counted_cards = Counter(line[0])
    value = find_value(counted_cards)
    sorted_cards = (''.join(line[0]))
    hands.add(Hand(cards=sorted_cards, bid=int(line[1]), value=value))

sorted_hands = (sorted(hands, key=lambda x: (x.value, x.cards)))
print(sorted_hands)
sum = 0
for i, hand in enumerate(sorted_hands):
    sum = sum + ((i + 1) * hand.bid)

print(str(sum))
