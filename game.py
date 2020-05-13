from deck import Deck
from hand import Hand


class Game:

    def __init__(self):
        self.deck = Deck()
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        self.deck.shuffle()

    def reset(self):
        self.deck.reset()
        self.dealer_hand.clear()
        self.player_hand.clear()
        self.deck.shuffle()

    def ask_user(self, prompt, valid_inputs):
        joined_inputs = '/'.join(valid_inputs)
        prompt_string = f'{prompt} ({joined_inputs})  '
        result = input(prompt_string)
        while result not in valid_inputs:
            print('Invalid input, please try again')
            result = input(prompt_string)
        return result

    def play_hand(self):
        # Setup and deal two cards to each player
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        # Print the game state
        self.display_game()

        user_input = self.ask_user('Choose:', ['hit', 'stay'])

        while user_input != 'stay' and not self.player_hand.is_bust():
            # Deal the player another card
            self.player_hand.add_card(self.deck.draw())
            self.display_game()
            if not self.player_hand.is_bust():
                user_input = self.ask_user('Choose:', ['hit', 'stay'])

        if self.player_hand.is_bust():
            print('Bust! You Lose!')
            return

        # If the player hasn't busted, dealer plays
        self.display_game(dealer_hidden=False)
        while self.dealer_hand.score() < 17:
            print('Dealer hits')
            self.dealer_hand.add_card(self.deck.draw())
            self.display_game(dealer_hidden=False)
            if self.dealer_hand.is_bust():
                print('Dealer busted! You Win!')
                return

        # Neither player has busted, who wins?

        if self.player_hand.score() > self.dealer_hand.score():
            print('You Win!')
        else:
            print('You Lose!')

    def display_game(self, dealer_hidden=True):
        print('Your hand:')
        print(self.player_hand.display())
        print(f'Score: {self.player_hand.score()}')
        print('Dealer\'s hand:')
        print(self.dealer_hand.display(dealer_hidden))

    def run(self):
        play_again = None
        while play_again != 'n':
            self.reset()
            self.play_hand()
            play_again = self.ask_user('Play again?', ['y', 'n'])


if __name__ == '__main__':
    game = Game()
    game.run()
