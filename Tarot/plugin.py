###
# All copyright waived via CC0. Written Sept 2021, by SirVo#
# 
# Tarot deck descriptions collected by sheoak: https://github.com/sheoak/tarot-deck
###

import random, json
from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *

try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Tarot')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

deck = {}

class Tarot(callbacks.Plugin):
    """Tarot deck simulator"""
    pass

    def __init__(self, irc):
        self.__parent = super(Tarot, self)
        self.__parent.__init__(irc)
        self.rng = random.Random()
        with open('./plugins/Tarot/cards.json') as deckFile:
            self.deck = json.loads(deckFile.read())

    def _reseed(self):
        self.rng.seed()
        
    def _reversalEnabled(self, irc, channel):
        """
        Check if reversed cards are enabled for this context.
        """
        return (irc.isChannel(channel) and self.registryValue("reversal", channel))

    def _artEnabled(self, irc, channel):
        """
        Check if appending card art URLs is enabled for this context.
        """
        return (irc.isChannel(channel) and self.registryValue("cardArt", channel))

    def draw(self, irc, msg, args, count):
        """[<number of cards>]

        Returns a number of tarot cards and automatically shuffles the deck after.
        A new time-based seed is used for every request.
        If only one card is requested, appends any available card art URLs.
        """
        self._reseed()
        art = ""

        # grab 'count' total key elements randomly from deck json
        drawn = random.choices(list(self.deck.keys()), k=count)

        # set default card orientation to upright
        rev = [0 for i in range(len(drawn))]

        # check if flipped cards are on, generate list of coin flips equal to count
        if self._reversalEnabled(irc, msg.channel):
            rev = [bool(random.getrandbits(1)) for i in drawn]

        # prep URL for assembly if: art is on, count is 1, json contains a URL
        if self._artEnabled(irc, msg.channel) and count == 1 and len(art) > 1:
            art = " - " + self.deck[drawn[0]]['art']

        irc.reply(', '.join(drawn[i] + ['', ' (r)'][rev[i]] + art for i in range(len(drawn))))

    draw = wrap(draw, [additional("positiveInt", 1)])

    def art(self, irc, msg, args, text):
        """<tarot card alias>

        Returns the card art link for a given tarot card, if available.
        Custom art URLs can be added to ./plugins/Tarot/cards.json
        """
        for k in self.deck.keys():
            if text.lower() == k.lower() or text.lower() in self.deck[k]['aliases']:
                card = k
                art = self.deck[k]['art']
                if 'http' in art:
                    irc.reply(card + ': ' + art)
                    return
                else:
                    irc.reply("There is no art available for this card. Make me some!")
                    return
        irc.reply(
            "Input does not match any card aliases, but here's a card picked randomly, especially for you! "
            + self.deck['The Fool']['art'])

    art = wrap(art, ['text'])

    def describe(self, irc, msg, args, text):
        """<tarot card alias>

        Returns the description of a given tarot card. Warning: can be quite verbose.
        """
        for k in self.deck.keys():
            if text.lower() == k.lower() or text.lower() in self.deck[k]['aliases']:
                card = k
                desc = self.deck[k]['desc']
                irc.reply(card + ': ' + desc)
                return
        irc.reply('No match found.')

    describe = wrap(describe, ['text'])

    def interpret(self, irc, msg, args, text):
        """<tarot card alias>

        Returns the interpretation for a given tarot card. Use the 'rinterpret' command for reversed cards.
        """
        card, interp = "", ""

        for k in self.deck.keys():
            if text.lower() == k.lower() or text.lower() in self.deck[k]['aliases']:
                card = k
                interp = self.deck[k]['interp']
                irc.reply(card + ': ' + interp)
                return
        irc.reply('No match found.')

    interpret = wrap(interpret, ['text'])

    def rinterpret(self, irc, msg, args, text):
        """<tarot card alias>

        Returns the interpretation for a given reversed tarot card. Use the 'interpret' command for upright cards.
        """
        card, interp = "", ""

        for k in self.deck.keys():
            if text.lower() == k.lower() or text.lower() in self.deck[k]['aliases']:
                card = k
                interp = self.deck[k]['interp_r']
                irc.reply(card + ' (r): ' + interp)
                return
        irc.reply('No match found.')
    rinterpret = wrap(rinterpret, ['text'])


Class = Tarot


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
