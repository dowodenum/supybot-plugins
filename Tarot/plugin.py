###
# Copyright (c) 2008, Andrey Rahmatullin
# Copyright (c) 2020, oddluck <oddluck@riseup.net>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###

from .deck import Deck

from operator import itemgetter
import re
import random
import sys,traceback

from supybot.commands import additional, wrap
from supybot.utils.str import format, ordinal
import supybot.ircmsgs as ircmsgs
import supybot.callbacks as callbacks


class Tarot(callbacks.Plugin):
    """This plugin supports drawing the cards using !draw 1 or !draw 2 etc.
    """

    def _process(self, irc, text):
        """
        Process a message and reply with draw results, if any.

        The message is split to the words and each word is checked against all
        known expression forms (first applicable form is used). All results
        are printed together in the IRC reply.
        """
        checklist = []
        results = []
        for word in text.split():
            for expr, parser in checklist:
                m = expr.match(word)
                if m:
                    r = parser(m)
                    if r:
                        results.append(r)
                        break
        if results:
            irc.reply("; ".join(results))

    def __init__(self, irc):
        self.__parent = super(Tarot, self)
        self.__parent.__init__(irc)
        self.deck = Deck()

    def _autoShuffleEnabled(self, irc, channel):
        """
        Check if automatic shuffling is enabled for this context.
        """
        return (irc.isChannel(channel) and self.registryValue("autoShuffle", channel))

    def shuffle(self, irc, msg, args):
        """takes no arguments

        Restores and shuffles the deck.
        """
        self.deck.shuffle()
        irc.reply("Tarot card deck shuffled.")

    shuffle = wrap(shuffle)

    def draw(self, irc, msg, args, count):
        """[<count>]

        Draws <count> cards (1 if omitted) from the deck and shows them.
        """
        cards = [next(self.deck) for i in range(count)]
        irc.reply(", ".join(cards))
        if self._autoShuffleEnabled(irc, msg.channel):
            self.deck.shuffle()

    draw = wrap(draw, [additional("positiveInt", 1)])
    deal = draw

    def doPrivmsg(self, irc, msg):
        if ircmsgs.isAction(msg):
            text = ircmsgs.unAction(msg)
        else:
            text = msg.args[1]
        self._process(irc, text)

Class = Tarot


# vim:set shiftwidth=4 tabstop=8 expandtab textwidth=78:
