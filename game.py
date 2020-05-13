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
        """
        Prompt the user with a question, and repeat until they give a valid answer
        For example, `self.ask_user('Choose:', ['hit', 'stay'])` will display:
          Choose: (hit/stay)
        and loop until the user types either hit or stay

        :param prompt: The question to display
        :param valid_inputs: the valid answers
        :return: one of the valid answers given
        """
        joined_inputs = '/'.join(valid_inputs)
        prompt_string = f'{prompt} ({joined_inputs})  '
        result = input(prompt_string)
        while result not in valid_inputs:
            print('Invalid input, please try again')
            result = input(prompt_string)
        return result

    def play_hand(self):
        # First, make sure everything is cleared out to play the hand
        self.reset()

        # Setup and deal two cards to each player
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())

        # Print the game state out to the user
        self.display_game()

        # Start by asking the user if they want to hit or stay
        user_input = self.ask_user('Choose:', ['hit', 'stay'])

        # Loop so long as the user is not busted and they have not entered "stay"
        while user_input != 'stay' and not self.player_hand.is_bust():
            # Deal the player another card
            self.player_hand.add_card(self.deck.draw())

            # Print out the game state again
            self.display_game()

            # Check if the user is busted and if so, return because the hand is done
            if self.player_hand.is_bust():
                print('Bust! You Lose!')
                return
            # Ask the user again if they'd like to hit, which determines if the loop will run again
            user_input = self.ask_user('Choose:', ['hit', 'stay'])

        # If the player hasn't busted, dealer plays
        # From here on out we don't mask the dealer's cards beyond the first
        self.display_game(dealer_hidden=False)
        # Dealers hit on 16 and stay on 17, so that's the condition for our loop
        while self.dealer_hand.score() < 17:
            print('Dealer hits')
            # Dealer draws a card
            self.dealer_hand.add_card(self.deck.draw())
            # Print out the game state again
            self.display_game(dealer_hidden=False)

            # Check if the dealer has busted and if so, return out of this function
            if self.dealer_hand.is_bust():
                print('Dealer busted! You Win!')
                return

        # Neither player has busted, who wins?

        if self.player_hand.score() > self.dealer_hand.score():
            print('You Win!')
        else:
            # Dealer wins in case of a tie
            print('You Lose!')

    def display_game(self, dealer_hidden=True):
        """
        Print out the game state to the console
        :param dealer_hidden: If cards in the dealers hand beyond the first should be "face down"
        :return: None
        """
        print('Your hand:')
        print(self.player_hand.display())
        print(f'Score: {self.player_hand.score()}')
        print('Dealer\'s hand:')
        print(self.dealer_hand.display(dealer_hidden))
        print()

    def run(self):
        """
        Main entry point to the game. Plays hands in a loop until the user chooses to exit
        :return: None
        """
        play_again = None
        while play_again != 'n':
            self.play_hand()
            play_again = self.ask_user('Play again?', ['y', 'n'])


if __name__ == '__main__':
    game = Game()
    game.run()
