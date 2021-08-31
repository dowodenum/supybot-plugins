Description
~~~~~~~~~~~
Tarot plugin contains the commands which simulate drawing of tarot cards.
The most basic feature of any deck plugin is, of course, drawing of one or several
cards and showing the results. That is what core 'draw' command can
do. It takes an expression such as 'draw 3' and returns a series of cards.

Deck
~~~~
A 78-card Marseilles deck which can be manually shuffled with the !shuffle command,
or set to shuffle automatically after each draw with the autoShuffle config setting.
The !draw X command displays the top X cards, removing them from the deck (unless 
autoShuffle is set). When the last card is drawn, the deck is automatically shuffled, 
but this is rare because you probably won't be using 78 cards in a single spread.
Also available is a reversal configuration paramter, allowing cards to be randomly
drawn upside-down. This occurs at the time of draw, not at the time of shuffle.

Thanks
~~~~~~
oddluck for Deck functions and overall plugin structure:
https://github.com/oddluck/limnoria-plugins/tree/master/Dice

