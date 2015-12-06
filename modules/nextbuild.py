#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module to print the next build number
"""

import urllib2
import json

user = '<ENTER_USER_NAME_HERE>'
token = '<ENTER_TOKEN_HERE>'
url = 'http://localhost:8080/view/App/api/json?depth=1&tree=jobs[name,lastBuild[number]]'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(None, url, user, token)

opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
handler = urllib2.urlopen(url)

payload = json.loads(handler.read())

max = 0

for job in payload['jobs']:  
    job_last_build = job['lastBuild']['number']
    if job_last_build > max:
        max = job_last_build

next = max + 1

print 'Next build number is {}'.format(next)
