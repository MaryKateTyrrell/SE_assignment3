'''
Created on 27 Feb 2018

@author: mary-katetyrrell
'''

import re
import requests

online = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
text = online.text.split('\n')

for line in text:
    parsing = pat.findall(line)
    print(parsing)