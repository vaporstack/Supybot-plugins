
###
# Copyright (c) 2016, vs
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

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import pyfiglet
from pyfiglet import Figlet

class Banner(callbacks.Plugin):
    """Add the help for "@plugin help Banner" here
    This should describe *how* to use this plugin."""

    def bannerfont(self, irc, msg, args, text):
        """[<number of sides>]
        
        rolls dice with n sides
        """
        try:
            f = Figlet(font=text)
            self.setRegistryValue('font', text)
            irc.replySuccess()
        except:
            irc.reply("Unable to set font! (see http://www.figlet.org )")
    bannerfont = wrap(bannerfont, [additional('text')])

    def banner(self, irc, msg, args, text):
        """PRINT STUFF ALL BEIG"""
        font = self.registryValue('font')
        f = Figlet(font=font)
        text = f.renderText(text).split("\n")
        text = [x for x in text if x.strip() != ""]
        for t in text:
            irc.reply(t)
        ##irc.reply("msg: %s" %  msg)
        #irc.reply("arg: %s" % args)
    banner = wrap(banner, [additional('text')])

Class = Banner


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
