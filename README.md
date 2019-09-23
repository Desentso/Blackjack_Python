# Blackjack

Command line Blackjack built with Python. It also has fancy ASCII cards.

## Requirements
> Python 3.x+ (tested on Python 3.5)

## How to run
`python src` or `python src/start.py`

## Example Game
    > python src/start.py
    Hello, welcome to play Blackjack!
    You have 100 coins, how much would you like to bet?
    Please enter a number between 1-100.
    > 5
    Your cards:
     _________   _________
    |4        | |5        |
    |         | |         |
    |         | |         |
    |    ^    | |    ^    |
    |         | |         |
    |         | |         |
    |________4| |________5|
    Total: 9

    Dealer's cards:
     _________   _________
    |J        | |---------|
    |         | |---------|
    |         | |---------|
    |    ^    | |---------|
    |         | |---------|
    |         | |---------|
    |________J| |_________|


    --------------------

    Your turn!
    Your cards:
     _________   _________
    |4        | |5        |
    |         | |         |
    |         | |         |
    |    ^    | |    ^    |
    |         | |         |
    |         | |         |
    |________4| |________5|
    Total: 9

    Would you like to
    [1] Hit
    [2] Stand
    > 1
    Your cards:
     _________   _________   _________
    |4        | |5        | |10       |
    |         | |         | |         |
    |         | |         | |         |
    |    ^    | |    ^    | |    o    |
    |         | |         | |         |
    |         | |         | |         |
    |________4| |________5| |_______10|
    Total: 19

    Would you like to
    [1] Hit
    [2] Stand
    [3] Double-down
    > 2
    Your cards:
     _________   _________   _________
    |4        | |5        | |10       |
    |         | |         | |         |
    |         | |         | |         |
    |    ^    | |    ^    | |    o    |
    |         | |         | |         |
    |         | |         | |         |
    |________4| |________5| |_______10|
    Total: 19

    --------------------

    Dealer's turn!
    ...

    --------------------

    Your cards:
     _________   _________   _________
    |4        | |5        | |10       |
    |         | |         | |         |
    |         | |         | |         |
    |    ^    | |    ^    | |    o    |
    |         | |         | |         |
    |         | |         | |         |
    |________4| |________5| |_______10|
    Total: 19

    Dealer's cards:
     _________   _________
    |J        | |J        |
    |         | |         |
    |         | |         |
    |    ^    | |    ^    |
    |         | |         |
    |         | |         |
    |________J| |________J|
    Total: 20

    DEALER WON!

    ...

## Card ASCII Art

     _________
    |2        |
    |         |
    |         |
    |    v    |
    |         |
    |         |
    |________2| 

     _________   _________   _________   _________   _________   _________   _________
    |2        | |3        | |10       | |J        | |K        | |Q        | |A        |
    |         | |         | |         | |         | |         | |         | |         |
    |         | |         | |         | |         | |         | |         | |         |
    |    v    | |    o    | |    &    | |    ^    | |    ^    | |    v    | |    o    |
    |         | |         | |         | |         | |         | |         | |         |
    |         | |         | |         | |         | |         | |         | |         |
    |________2| |________3| |_______10| |________J| |________K| |________Q| |________A|
