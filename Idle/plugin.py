###
# Copyright (c) 2010, futurestack
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

from BeautifulSoup import BeautifulSoup
import urllib2

class Idle(callbacks.Plugin):
    """Add the help for "@plugin help Blank" here
    This should describe *how* to use this plugin."""
    

    def __init__(self, irc):
        self.__parent = super(Idle, self)
        self.__parent.__init__(irc)
        #self.cachedData = []
        
        
        #self.rng = random.Random()   # create our rng
        #self.rng.seed()   # automatically seeds with current time
        #f = open("./plugins/Jabbar/data/bender.txt",'r')
        #self.benderquotes = f.readlines()
        #f.close()
        #self.adamsquotes = myReadFile('./plugins/Jabbar/data/adams.txt')



    def idle(self, irc, msg, args, text):
        """Usage: idle <playername>.  This plugin scrapes https://www.anderdonau.de/nethackidle/players.php and returns player info.
        """                
        response = "Couldn't find that player."
        if (text == None ):
            response = "Please input a player name."
            irc.reply(response)
            return
            
        page = urllib2.urlopen("https://www.anderdonau.de/nethackidle/players.php")
        #f = open("http://pallas.crash-override.net/nethackidle/players.php")
        #doc = f.read()
        #f.close()
        soup = BeautifulSoup(''.join(page))

        results = soup.findAll('li')

        player = ""
        print("Searching %s items for %s..." % ( str(len(results)), text) )
        found = False;
        textLowered = text.lower()
        print("Text is now %s" % textLowered)
        
        for item in results:
            itemString = "" + str(item)
            itemString = itemString.lower()
            resultIndex = itemString.find( textLowered )
            if (resultIndex != -1 ):
                player = item
                found = True
                print("Found!")
                break

        if found :
            data = str(player);
            offline = data.find("offline")
            if( offline > -1 ):
                response = text + " is offline."

            data = data.replace("<li>","")
            data = data.replace("</li>","")
            data = data.replace("</a>","")
            data = data.replace('">',"")
            range = data.lower().find(text.lower())
            #data = data[range:]
            length = len(text)
            print(length)
            data = data[length:]
            print("DATA:%s" % data)

            if( offline == -1 ):
                response = data
            else:
                response = "That player is offline."
            #print("Response:%s" % response)

        print("Response:%s" % response)
        
        irc.reply(response)
    idle = wrap(idle, [additional('text')])

           
        
        
        
Class = Idle


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
