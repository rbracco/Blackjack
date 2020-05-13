class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        score = 0
        num_aces = 0
        for card in self.cards:
            if card.is_facecard():
                score += 10
            elif card.rank == 1:
                num_aces += 1
                score += 11
            else:
                score += card.rank
        while score > 21 and num_aces > 0:
            score -= 10
            num_aces -= 1
        return score

    def is_bust(self):
        return self.score() > 21

    def clear(self):
        self.cards = []

    def shown_card(self):
        if len(self.cards) > 0:
            return self.cards[0]
        else:
            return None

    def display(self, hidden=False):
        if hidden:
            card_strings = []
            for index in range(len(self.cards)):
                if index == 0:
                    card_strings.append(str(self.cards[index]))
                else:
                    card_strings.append('[Card]')
        else:
            card_strings = [str(card) for card in self.cards]
        return ', '.join(card_strings)
