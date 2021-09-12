###
# All copyright waived via CC0. Written Sept 2021, by SirVo#
# 
# Tarot deck descriptions collected by sheoak: https://github.com/sheoak/tarot-deck
###

"""
Tarot: Tarot deck simulator.
"""

import sys
import supybot
from supybot import world

# Use this for the version of this plugin.
__version__ = "0.1"

# XXX Replace this with an appropriate author or supybot.Author instance.
__author__ = supybot.Author('SirVo', 'SirVo',
                            'TheSirVo@protonmail.com')

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

# This is a url where the most recent plugin package can be downloaded.
__url__ = 'https://github.com/dowodenum/supybot-plugins/tree/main/Tarot'

from . import config
from . import plugin
if sys.version_info >= (3, 4):
    from importlib import reload
else:
    from imp import reload
# In case we're being reloaded.
reload(config)
reload(plugin)
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    from . import test

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
