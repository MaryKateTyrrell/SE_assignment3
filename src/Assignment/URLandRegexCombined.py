'''
Created on 27 Feb 2018

@author: mary-katetyrrell
'''

import re
import requests

online = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
file = online.text.split('\n')

for line in file[:1]:
    length = line
    print(line)
    
for line in file[1:-1]:
    m = pat.match(line)
    command = m.group(1)
    x1 = m.group(2)
    x2 = m.group(3)
    y1 = m.group(4)
    y2 = m.group(5)
    arr =[command, x1, x2, y1, y2]
    print(arr)
    
    
   
    
    

'''pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
#practice parsing the file. 
m = pat.match("turn on 247,321 through 1053,1053")
command = m.group()
command = m.group(1)
x1 = m.group(2)
x2 = m.group(3)
y1 = m.group(4)
y2 = m.group(5)

print( x1, x2, y1, y2)'''