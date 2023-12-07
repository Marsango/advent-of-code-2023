deck = 'J23456789TQKA'


class hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        type = 0
        current_type = 0
        has_a_pair = 0
        has_double_pair: 0
        has_a_three = 0
        for deck_card in deck.strip('J'):
            count = cards.count(deck_card)
            if count == 5:
                current_type = 6
            elif count == 4:
                current_type = 5
            elif count == 3:
                if has_a_pair:
                    current_type = 4
                else:
                    has_a_three = 1
                    current_type = 3
            elif count == 2:
                if has_a_three:
                    current_type = 4
                elif not has_a_pair:
                    has_a_pair = 1
                    current_type = 1
                else:
                    has_double_pair = 1
                    current_type = 2
            else:
                current_type = 0
            if current_type > type:
                type = current_type
        if "J" in cards:
            if 1 == cards.count('J'):
                match type:
                    case 0:
                        type = 1
                    case 1:
                        type = 3
                    case 2:
                        type = 4
                    case 3:
                        type = 5
                    case 4:
                        type = 6
                    case 5:
                        type = 6
            elif 2 == cards.count('J'):
                match type:
                    case 0:
                        type = 3
                    case 1:
                        type = 5
                    case 3:
                        type = 6
            elif 3 == cards.count('J'):
                match type:
                    case 0:
                        type = 5
                    case 1:
                        type = 6
            else:
                type  = 6
        self.type = int(type)

    def __repr__(self):
        return f'{self.cards}  {self.bid} {self.type} |'


def input_function():
    list_of_hands = []
    with open('input.txt') as f:
        string = f.readlines()
    for line in string:
        aux = line.strip('\n').split(' ')
        list_of_hands.append(hand(aux[0], aux[1]))
    return list_of_hands


def calculate_total_winnings(list_of_hands):
    total_winnings = 0
    for i in range(len(list_of_hands)):
        for j in range(len(list_of_hands)):
            if list_of_hands[i].type < list_of_hands[j].type:
                aux = list_of_hands[i]
                list_of_hands[i] = list_of_hands[j]
                list_of_hands[j] = aux
            elif list_of_hands[i].type == list_of_hands[j].type and list_of_hands[i] != list_of_hands[j]:
                current_card = 0
                while list_of_hands[i].cards[current_card] == list_of_hands[j].cards[current_card]:
                    current_card += 1
                if deck.find(list_of_hands[i].cards[current_card]) < deck.find(list_of_hands[j].cards[current_card]):
                    aux = list_of_hands[i]
                    list_of_hands[i] = list_of_hands[j]
                    list_of_hands[j] = aux
    for k, hands in enumerate(list_of_hands):
        total_winnings += hands.bid * (k + 1)
    print(total_winnings)


if __name__ == '__main__':
    calculate_total_winnings(input_function())