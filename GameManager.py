import random


def number_elements_greater_equal_or_less(coll, value):
    number_greater = 0
    number_equal = 0
    number_less = 0
    for i in coll:
        if i > value:
            number_greater += 1
        elif i < value:
            number_less += 1
        elif i == value:
            number_equal += 1

    return number_greater, number_equal, number_less


class GameManager:
    def __init__(self):
        self.cards = [("6C.png", 6), ("6S.png", 6), ("6D.png", 6), ("6H.png", 6),
                      ("7C.png", 7), ("7S.png", 7), ("7D.png", 7), ("7H.png", 7),
                      ("8C.png", 8), ("8S.png", 8), ("8D.png", 8), ("8H.png", 8),
                      ("9C.png", 9), ("9S.png", 9), ("9D.png", 9), ("9H.png", 9),
                      ("10C.png", 10), ("10S.png", 10), ("10D.png", 10), ("10H.png", 10),
                      ("JC.png", 11), ("JS.png", 11), ("JD.png", 11), ("JH.png", 11),
                      ("QC.png", 12), ("QS.png", 12), ("QD.png", 12), ("QH.png", 12),
                      ("KC.png", 13), ("KS.png", 13), ("KD.png", 13), ("KH.png", 13),
                      ("AC.png", 14), ("AS.png", 14), ("AD.png", 14), ("AH.png", 14)]
        self.iterator = 0
        self.win_number = 0
        self.answers = []
        self.expected_answers = []
        self.probabilities = []
        self.is_end = False
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def calculate_probabilities(self):
        card_costs = [6, 6, 6, 6,
             7, 7, 7, 7,
             8, 8, 8, 8,
             9, 9, 9, 9,
             10, 10, 10, 10,
             11, 11, 11, 11,
             12, 12, 12, 12,
             13, 13, 13, 13,
             14, 14, 14, 14]

        for i in range(len(self.cards) - 1):
            card_costs.remove(self.cards[i][1])
            greater, equal, less = (number_elements_greater_equal_or_less(card_costs, self.cards[i][1]))
            self.probabilities.append(tuple([round(greater / len(card_costs), 2),
                                        round(equal / len(card_costs), 2),
                                        round(less / len(card_costs), 2)]))
            expected_choice = self.probabilities[-1].index(max(self.probabilities[-1]))
            if expected_choice == 0:
                self.expected_answers.append(1)
            elif expected_choice == 1:
                self.expected_answers.append(0)
            elif expected_choice == 2:
                self.expected_answers.append(-1)

        print(self.probabilities)
        print(self.expected_answers)

    def get_next_card(self):
        self.iterator += 1
        card = self.cards[self.iterator]

        print("Iterator_1: " + str(self.iterator))
        if self.iterator == 35:
            self.is_end = True
            self.calculate_probabilities()

        return card, self.is_end

    def get_current_card(self):
        card = self.cards[self.iterator]
        return card

    def check_answer(self, state):
        self.answers.append(state)
        if state == 1:
            if self.cards[self.iterator][1] > self.cards[self.iterator - 1][1]:
                self.win_number += 1
                return True
        elif state == 0:
            if self.cards[self.iterator][1] == self.cards[self.iterator - 1][1]:
                self.win_number += 1
                return True
        elif state == -1:
            if self.cards[self.iterator][1] < self.cards[self.iterator - 1][1]:
                self.win_number += 1
                return True

        return False

    def clear(self):
        self.iterator = 0
        self.win_number = 0
        self.answers = []
        self.expected_answers = []
        self.probabilities = []
        self.is_end = False

        self.shuffle_deck()
