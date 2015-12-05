#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Proverb module, using sprichwortgenerator.de, to print random proverbs
"""

url = 'http://sprichwort.gener.at/or/' # english: 'http://proverb.gener.at/or/'

from bs4 import BeautifulSoup
import urllib2

response = urllib2.urlopen(url)
html = response.read()

parsed_html = BeautifulSoup(html, "html.parser")
print parsed_html.body.find('div', attrs={'class':'spwort'}).text.encode('utf-8')
