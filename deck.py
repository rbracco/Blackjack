from card import Card
from random import randrange


class Deck:

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.cards.append(Card(rank, suit))

    def draw(self):
        """
        draws the first card from the deck, removes it, and returns it
        :return: the drawn [Card]
        """
        return self.cards.pop(0)

    def shuffle(self):
        """
        randomizes the order of the cards in the deck
        :return: None
        """
        new_deck = []
        while len(self.cards) > 0:
            index_to_remove = randrange(len(self.cards))
            removed_card = self.cards.pop(index_to_remove)
            new_deck.append(removed_card)
        self.cards = new_deck

