###
# Copyright (c) 2008, Anatoly Popov
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

import random


class Deck:
    """
    78-card tarot deck simulator.

    This class represents a standard 78-card deck (with 22 major Arcana)
    and supports shuffling and drawing.
    """

    titles = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]
    titles = [a + " of " for a in titles]
    suits = ["Wands", "Cups", "Swords", "Pentacles"]

    def __init__(self):
        """
        Initialize a new deck and shuffle it.
        """
        self.deck = []
        self.base_deck = ["The Fool", "The Magician", "The High Priestess", "The Empress",
                          "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
                          "Strength", "The Hermit", "The Wheel of Fortune", "Justice",
                          "The Hanged Man", "Death", "Temperance", "The Devil",
                          "The Tower", "The Star", "The Moon", "The Sun",
                          "Judgement", "The World"] + [t + s for t in self.titles for s in self.suits]
        self.shuffle()

    def shuffle(self):
        """
        Restore and shuffle the deck.

        All cards are returned to the deck and then shuffled randomly.
        """
        new_deck = self.base_deck[:]
        random.shuffle(new_deck)
        self.deck = new_deck

    def __next__(self):
        """
        Draw the top card from the deck and return it.

        Drawn card is removed from the deck. If it was the last card, deck is
        shuffled.
        """
        card = self.deck.pop()
        if not self.deck:
            self.shuffle()
        return card
