'''
Created on 27 Feb 2018

@author: mary-katetyrrell
'''
import urllib

online = urllib.urlopen("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
for line in online:
    print(line)