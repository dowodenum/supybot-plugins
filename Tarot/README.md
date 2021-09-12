Tarot deck simulator.

## Deck

Uses a 78-card Marseilles deck.

## Draw

Using 'draw X', the bot will draw multiple unique cards from the deck for you.
If no X is given, bot assumes you want just one card.
A new time-based seed is given to Python's Random module for each draw command.

## Reversal

If the plugins.Tarot.reversal config setting is set True, coin flips are done
at the time of draw to determine whether each card drawn is inverted.

## Describe

Using 'describe <alias>' the user can request the bot to read out a (verbose)
artistic description of the card.

## Interpret

Using either 'interpret <alias>' or 'rinterpret <alias>' the user can get an
interpretation of the card from the bot, for upright or inverted cards, respectively.

## Art

Custom art URLs can be added to the cards.json file, in URL format. If the
plugins.Tarot.cardArt config setting is True, then these will be appended to single
card draws. The art URL can be requested on its own with the 'art <alias>' command.

## Aliases

You can use typical alternate spellings (judgement/judgment) as well as short codes.
For the Major Arcana, numbers 0-21 and roman numerals I-XXI will work.
For Minor Arcana, short codes like '2ow' for 'Two of Wands' or 'know' for Knight
of Pentacles.

Examples: 
"tower" -> "The Tower"
"wheel" -> "The Wheel of Fortune"
"aoc" -> "Ace of Cups"
"kos" -> "King of Swords"

## Thanks

oddluck for Deck functions and overall plugin structure 
(I've since rewritten this from scratch, with the main change being the utilization 
of Python's Random.choices() function)
https://github.com/oddluck/limnoria-plugins/tree/master/Dice

cottongin for Python troubleshooting and code advice:
https://github.com/cottongin/StreamStuff/

sheoak for collecting descriptions/interpretations into a nice CSV file:
https://github.com/sheoak/tarot-deck