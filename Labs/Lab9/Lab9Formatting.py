# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 00:15:35 2022

@author: maxwe
"""


import json

import requests

print

r = requests.get('http://localhost:3000/')

data = r.json()

print(data[0]["name"] + " is " + data[0]["color"])
print(data[1]["name"] + " is " + data[1]["color"])
print(data[2]["name"] + " is " + data[2]["color"])
print(data[3]["name"] + " is " + data[3]["color"])



