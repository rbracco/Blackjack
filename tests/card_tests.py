import unittest

from card import Card


class CardTestCase(unittest.TestCase):
    def test_str_with_card(self):
        card = Card(1, Card.SPADES)
        self.assertEqual('Ace of Spades', str(card))

    def test_is_facecard_for_king(self):
        card = Card(13, Card.HEARTS)
        self.assertTrue(card.is_facecard())


if __name__ == '__main__':
    unittest.main()
