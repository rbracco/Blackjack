class Card:
    SPADES = 'Spades'
    HEARTS = 'Hearts'
    CLUBS = 'Clubs'
    DIAMONDS = 'Diamonds'

    RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    SUITS = [SPADES, HEARTS, CLUBS, DIAMONDS]

    def __init__(self, rank, suit):
        if rank not in Card.RANKS:
            raise Exception(f'Invalid rank: {rank}')
        if suit not in Card.SUITS:
            raise Exception(f'Invalid suit: {suit}')

        self.rank = rank
        self.suit = suit

    def format_rank(self):
        if self.rank == 1:
            return 'Ace'
        elif self.rank < 11:
            return str(self.rank)
        elif self.rank == 11:
            return 'Jack'
        elif self.rank == 12:
            return 'Queen'
        elif self.rank == 13:
            return 'King'
        else:
            raise Exception(f'Invalid rank: {self.rank}')

    def is_facecard(self):
        return self.rank in [11, 12, 13]

    def __str__(self):
        return f'{self.format_rank()} of {self.suit}'
