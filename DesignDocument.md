The game was built using object-oriented design pattern. There are three classes Game, Player and Card. Each one has a one clear purpose that they handle. Also the Player class gets a nice reuse also as the dealer.


## Classes
The Game class handles running the game and the logic. For example it has the logic how the game should flow, e.g. what happens when player overdraws, or gets a blackjack. It handles the turns for both player and dealer. It also checks the win condition and lose condition. In general it handles everything that is not directly related to Card or Player specific methods.

The Player class handles the logic for the player and encloses the player/dealer specific variable such as cards, current bet, hand total value and money. 

The Card class stores the card values and regions, it also handles the logic for printing the ASCII art cards.


## Data structures
List was used to store the cards, because it's easy and efficient to store the cards and also to do random index retrieves.
Cards were instances of the Card class, which holds the value and suit of the card. Which made it easy to print the ASCII art of the specific card.


## Algorithms
To draw a card we simply generated a random index between 0 and the cards length - 1, which was the index of the card that was drawn. Another solution could have been to shuffle the cards first and then pop them one by one.


## Tooling
Python was chosen because it's easy to work with. Also it has an expansive standard library, which makes it easy and quick to develop with. Also the minimalistic syntax makes it fast to develop. Also in a project this small something like static typing doesn't give that much of a benefit, also performance differences are negligible.

For testing the Python's default unittest library was chosen, because it offers all of the basic testing tools and test runner needed for this project. It's included by default and has easy to use test runner.

No external libraries are used in this project.

## Testing
Tests were built using the unittest library that is included by default. Unit and small integration tests were built for each class. The tests test the most critical methods and logic. For some methods mocking/stubbing is used to gather the required information to the assertions, for example how many times the function was called and with which parameters.