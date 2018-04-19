###
# Copyright (c) 2011, Valentin Lorentz
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
from pyfiglet import Figlet
import glob


class Birthday(callbacks.Plugin):
    """Add the help for "@plugin help Birthday" here
    This should describe *how* to use this plugin."""

    def birthday_fonts(self,irc,msg,args,text):
        """prints the fonts"""
        fonts = glob.glob("/usr/local/lib/python2.6/dist-packages/pyfiglet/fonts/*.flf")
        accum = []
        for f in fonts:
            accum.append(f.replace(".flf",""))
        irc.reply( ",".join(accum) )
    birthday_fonts = wrap(birthday_fonts,[additional('text')])

    def birthday(self, irc, msg, args,text):
        """takes no arguments
            """
 	print text       
        def obnoxious(text, font=None):
	    if font is None:

                f = Figlet('poison')
            else:
                f = Figlet(font)
 
            data = f.renderText(text)
            print data
	    data = data.split("\n");
	    for line in data:
                #line = line.strip()
                if line is not "":
                    irc.reply(line)
        print "args"
	print args 
        #obnoxious("HAPPY")
        #obnoxious("BIRTHDAY")
        irc.reply(" *  H A P P Y   B I R T H D A Y *  ")
        obnoxious(text)

    birthday = wrap(birthday, [additional('text')])


Class = Birthday


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
