'''
Created on 1 Mar 2018

@author: mary-katetyrrell
'''
import sys
import re
import requests
from fileinput import filename


online = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
file = online.text.split('\n')


 
class lightTest():
    
    lights = None
    lightcounter = 0
    
    '''
    this class will test the number of lights that are left on
    
    '''
    def __init__(self, size):
        
        '''initialize the multidimensional array, to the size of the input 
        or the first line in the file'''
        
        self.size = size
        self.lights = [[False]*size for _ in range(size)]
        
    def command(self, c, y1, x1, y2, x2):
        
        '''Take in the parsed variables and use them accordingly'''
    
        self.c = c  #corresponds to group1
        self.x1 = x1  #corresponds to group2
        self.y1 = y1    #corresponds to group3
        self.x2 = x2    #corresponds to group4
        self.y2 = y2    #corresponds to group5
        
        '''check the nature of the commands and adjust the coordinates as so
        turn on - turn those coordinates to true
        turn off - turn those coordinates to false
        switch - turn the coordinates to true and the others off'''
        
        if self.c == "turn on":
            
            for i in (self.x1,self.x2):
                for j in (self.y1, self.y2):
                    self.lights[i][j] = True
                
        if self.c == "turn off":
            for i in (self.x1,self.x2):
                for j in (self.y1, self.y2):
                    self.lights[i][j] = False
                      
        if self.c == "switch":
            for i in (self.x1,self.x2):
                for j in (self.y1, self.y2):
                    if self.lights[i][j] == True:
                        self.lights[i][j] = False
                    if self.lights[i][j] == False:
                        self.lights[i][j] = True
                        
        for i in self.lights:
            
            '''count the number of coordinates that are True
            note: this is a multidimensional set up,
            thought process was - square multiplication table from
            programming '''
            
            for j in i:
                if j == True:
                    self.lightcounter +=1
        print("there are now", self.lightcounter, "lights turned on")
        
        
                        
for line in file[:1]:
    length = int(line)
    switchboard = lightTest(length)
for line in file[1:-1]:
        m = pat.match(line)
        command = m.group(1)
        y1 = m.group(2)
        x1 = m.group(3)
        y2 = m.group(4)
        x2 = m.group(5)
        switchboard.command(command, int(y1), int(x1), int(y2), int(x2))
    
  
        
        
       





