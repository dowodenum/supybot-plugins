Tarot deck plugin.

Forked from https://github.com/oddluck/limnoria-plugins/tree/master/Dice

Install dependencies: python3 -m pip install -r requirements.txt

## Description

Tarot plugin contains the commands which simulate drawing of tarot cards.
The most basic feature of any deck plugin is, of course, drawing of one or 
several cards and showing the results. That is what core 'draw' command can
do. It takes an expression such as 'draw 3' and returns a series of cards.

## Deck

Bot has a 78-card Marseilles deck which it can shuffle (!shuffle command)
and from which you can draw (!draw or !deal command, with optional number
argument if you want to draw several cards). Drawn card is removed from
the deck, but shuffle restores full deck. If the last card is drawn, the
deck is automatically shuffled before drawing next card.

## Thanks

oddluck for Deck functions and overall plugin structure:
https://github.com/oddluck/limnoria-plugins/tree/master/Dice

