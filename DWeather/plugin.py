###
# Copyright (c) 2014, fs
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
import urllib2
import json
import subprocess
import random

def gendoge(data):
    res = " very doge."
    #print data
    data = data.split()
    adverbs = "very much such so".split()
    accum = []
    for d in data:
        if d != "a" and d != "of":
            accum.append(d.lower() )

    #print accum
    lines = []
    for a in accum:
        l = random.choice(adverbs) + " " + a
        lines.append( l )
    res = ", ".join(lines)

    return res

class DWeather(callbacks.Plugin):
    """Add the help for "@plugin help DWeather" here
    This should describe *how* to use this plugin."""
    #threaded = True
    
    def weather(self, irc, msg, args, text):
        """Does the weather??

        """
        result = "No result."        
        #print text	
        text = text.replace(' ','%20')
        city = str(text);
        #print city
	#theurl = 'http://api.wunderground.com/api/8a594dbc71a8382c/geolookup/conditions/q/IA/%s.json' % city
        cmd = 'python /usr/local/lib/python2.7/dist-packages/pycliweather/pycliweather.py %s' % city
        res = subprocess.check_output(cmd, shell=True)
        #print res
        #f = urllib2.urlopen(theurl)
        #json_string = f.read()
        #parsed_json = json.loads(json_string)
        #location = parsed_json['location']['city']
        #temp_f = parsed_json['current_observation']['temp_f']
        #result = "Current temperature in %s is: %s" % (location, temp_f)
        #location = parsed_json['location']['city']
        #temp_c = parsed_json['current_observation']['temp_c']
        #weather = parsed_json['current_observation']['weather']
        #feelslike_c = parsed_json['current_observation']['feelslike_c']
        #wind_kph = parsed_json['current_observation']['wind_kph']
        #wind_gust_kph = parsed_json['current_observation']['wind_gust_kph']
        #wind_dir = parsed_json['current_observation']['wind_dir']
        #wind_degrees = parsed_json['current_observation']['wind_degrees']
        #print parsed_json
        
        lines = res.split("\n")
        print lines	
        loc = lines[0].split(":")[-1:][0].strip()
        today = lines[5].split("-")
        conditions = today[1].strip()
        temps = today[2].strip()
        #print today
        #print loc
        response = loc + " : " + temps
        cdata = gendoge(conditions)
        #print cdata
        response = response + ". " + cdata
        response = response.replace("%20"," ")
        irc.reply(response)

    weather = wrap(weather, [additional('text')])



Class = DWeather


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
