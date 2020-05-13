import unittest

from card import Card
from deck import Deck
from hand import Hand


class CardTestCase(unittest.TestCase):
    def test_str_with_card(self):
        card = Card(1, Card.SPADES)
        self.assertEqual('Ace of Spades', str(card))

    def test_is_facecard_for_king(self):
        card = Card(13, Card.HEARTS)
        self.assertTrue(card.is_facecard())


class HandTestCase(unittest.TestCase):
    def test_three_kings_is_bust(self):
        hand = Hand()
        hand.add_card(Card(13, Card.SPADES))
        hand.add_card(Card(13, Card.HEARTS))
        hand.add_card(Card(13, Card.CLUBS))

        self.assertTrue(hand.is_bust())


class DeckTestCase(unittest.TestCase):
    def test_initial_deck_has_52_cards(self):
        deck = Deck()

        self.assertEqual(len(deck.cards), 52)

    def test_draw_returns_top_card(self):
        deck = Deck()
        top_card = deck.cards[0]

        drawn_card = deck.draw()

        self.assertEqual(top_card.rank, drawn_card.rank)
        self.assertEqual(top_card.suit, drawn_card.suit)

    def test_drawing_reduces_deck_size_by_1(self):
        deck = Deck()
        initial_size = len(deck.cards)
        deck.draw()
        size = len(deck.cards)

        self.assertEqual(size, initial_size - 1)


if __name__ == '__main__':
    unittest.main()
