import random


class GameManager:
    def __init__(self):
        # self.cards = [("6 крест", 6), ("6 пик", 6), ("6 черв", 6), ("6 бубей", 6),
        #               ("7 крест", 7), ("7 пик", 7), ("7 черв", 7), ("7 бубей", 7),
        #               ("8 крест", 8), ("8 пик", 8), ("8 черв", 8), ("8 бубей", 8),
        #               ("9 крест", 9), ("9 пик", 9), ("9 черв", 9), ("9 бубей", 9),
        #               ("10 крест", 10), ("10 пик", 10), ("10 черв", 10), ("10 бубей", 10),
        #               ("Валет крест", 11), ("Валет пик", 11), ("Валет черв", 11), ("Валет бубей", 11),
        #               ("Дама крест", 12), ("Дама пик", 12), ("Дама черв", 12), ("Дама бубей", 12),
        #               ("Король крест", 13), ("Король пик", 13), ("Король черв", 13), ("Король бубей", 13),
        #               ("Туз крест", 14), ("Туз пик", 14), ("Туз черв", 14), ("Туз бубей", 14)]

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
        self.is_end = False
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def get_next_card(self):
        self.iterator += 1
        card = self.cards[self.iterator]

        print("Iterator_1: " + str(self.iterator))
        if self.iterator == 35:
            self.is_end = True

        return card, self.is_end

    def get_current_card(self):
        card = self.cards[self.iterator]
        return card

    def check_answer(self, state):
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
