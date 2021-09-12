###
# All copyright waived via CC0. Written Sept 2021, by SirVo#
# 
# Tarot deck descriptions collected by sheoak: https://github.com/sheoak/tarot-deck
###

from supybot import conf, registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Tarot')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Tarot', True)

    conf.registerChannelValue(
        Tarot,
        "reversal",
        registry.Boolean(
            False,
            _(
                """
                Whether inverted cards should be generated.
                Determined by coin flip at time of selection.
                """
            ),
        ),
    )

    conf.registerChannelValue(
        Tarot,
        "cardArt",
        registry.Boolean(
            False,
            _(
                """
                Whether card art URLs should be added to single-draw command replies. 
                Specify art URLs in dict format in the cardArt.txt file, located in the plugin directory. 
                """
            ),
        ),
    )

Tarot = conf.registerPlugin('Tarot')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Tarot, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
