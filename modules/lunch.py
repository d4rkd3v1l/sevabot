#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A dice roll module
"""
import sys
import random
import os

locations = ['location1', 'location2', 'location3']

random.seed()

location = locations[random.randint(0, len(locations)-1)]

print 'What about {}?'.format(location)
