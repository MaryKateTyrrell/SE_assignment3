'''
Created on 26 Feb 2018

@author: mary-katetyrrell

'''

import re
pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
#practice parsing the file. 
m = pat.match("turn on 247,321 through 1053,1053")
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))
print(m.group(5))


