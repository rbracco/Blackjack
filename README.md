# Blackjack

#### Sample CodeLouisville Project

A simple command line Blackjack game

## Installation & Running

This project uses `Pipenv` to run.

* Check out the source code locally
* Inside the project dir, run `pipenv install`
* Run `pipenv run python game.py`

## Tests

Once your environment is set up, you can run tests with:

* `pipenv run python tests.py`
 
## Source Overview

This project consists of a few classes:

* `Card` is a simple datastructure containing a `rank` and `suit` value
    * It contains an `is_facecard()` method to check if it is a face card
* `Hand` is a class with the following properties:
    * `cards`: A list of `Card` objects in the hand
    * `add_card(card)`: A method to put the given card into the hand
    * `score()`: computes the Blackjack score for the hand
    * `is_bust()`: returns True if the score is over 21
* `Deck` is a class representing the yet-undrawn cards in the Deck.
    * It is initialized as a standard deck of 52 playing cards
    * `shuffle()`: randomizes the order of the cards
    * `draw()`: removes the top card from the deck and returns it.
    
The game loop logic itself is contained in the `Game` class. Check the comments in that file for more information