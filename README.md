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

### Requirements:

This project fulfills the following requirements:

* Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
    * There are two such loops. The outer "Play again" one and the inner "hit/stay" loop. Both are in `game.py`
* Create a class, then create at least one object of that class and populate it with data
    * All of `Card`, `Hand`, and `Deck` qualify
* Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
    * Both `Hand` and `Deck` use a list internally to store their data
* Create and call at least 3 functions, at least one of which must return a value that is used
    * So many functions. In particular `draw()` returns a value, a `Card` that is used
* Create 3 or more unit tests for your application
    * They reside in `tests.py`

#### Additional Requirements
* Your code have comments that document major sections of your code to make it easier to read
    * Both inline comments and pydoc comments on the functions themselves
* Your project code is uploaded to your GitHub account, in its own repository, with at least 5 commits
* We need to see that you’ve used Git to update your GitHub profile at least 5 times
* It must include a README file located at the top level directory of your project that includes:
    * (You're reading it!)
    * A description of your project
    * What features you chose to included (so we know what to look for)
    * Any special instructions we might need to run your project
