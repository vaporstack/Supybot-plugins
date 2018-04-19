###
# Copyright (c) 2013, futurestack
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
import supybot.conf as conf

class InTheBeginning(callbacks.Plugin):
    """Add the help for "@plugin help InTheBeginning" here
    This should describe *how* to use this plugin."""
    pass

    def __init__(self,irc):
        self.__parent = super(InTheBeginning, self)
        self.__parent.__init__(irc)
        self.position = conf.supybot.plugins.InTheBeginning.position

        pass
        #self.position = self.registryValue('position',channel)
        #self.position = 
    def myReadFile(self, path):
        """reads a file to a list"""
        f = open(path,'r')
        result = f.readlines()
        f.close
        return result



    def commandline(self, irc, msg, args):
        """Reads the next bit from In The Beginning Was The Command Line."""
        channel = msg.args[0];
        counter = self.registryValue('position', channel) 
        data = self.myReadFile('plugins/InTheBeginning/data/command_stripped.txt')
        result = data[counter].strip()        
        #i#counter = self.registryValue('position'
        counter = counter + 1
        self.position.setValue(counter) 
        #conf.registerChannelValue( InTheBeginning, 'position', registry.PositiveInteger( counter,
        #counter.setValue( counter + 1 )
        irc.reply( result )
    
    commandline = wrap(commandline);

Class = InTheBeginning
# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
