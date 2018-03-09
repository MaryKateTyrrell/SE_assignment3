'''
Created on 1 Mar 2018

@author: mary-katetyrrell
'''
import sys
import re
import requests
from fileinput import filename

#file = requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
#file = online.text.split('\n')

class lightTest():
    
    lights = None
     
    '''
    this class will test the number of lights that are left on
    
    '''
    def __init__(self, size):
        
        '''initialize the multidimensional array, to the size of the input 
        or the first line in the file'''
        
        self.size = size
        self.lights = [[False]*size for _ in range(size)]
        
    def command(self, c, x1, y1, x2, y2):
        
        #Need to make sure that the coordinates remain within the boundaries of size
        #Making the cordinates equal to size if they are beyond it.
        #found due to error in input file.
        
        #still getting an index out of range error - trying to -1, because we start counting from zero
        #so if we start from zero we want to continue to 999. 
        if x1 < 0:
            x1 = 0
        if x2 < 0:
            x2 = 0
        if y1 < 0:
            y1 = 0
        if y2 < 0:
            y2 = 0
        if x1 > self.size-1:
            x1 = self.size -1
        if x2 > self.size-1:
            x2 = self.size-1
        if y1 > self.size-1:
            y1 = self.size-1
        if y2 > self.size-1:
            y2 = self.size-1
        
        '''Take in the parsed variables and use them accordingly'''
        
        '''check the nature of the commands and adjust the coordinates as so
        turn on - turn those coordinates to true
        turn off - turn those coordinates to false
        switch - turn the coordinates to true and the others off'''
        
        if c == "turn on" or c == "turn on ":
            for i in range(min(y1, y2), max(y1, y2)+1):
                for j in range(min(x1,x2), max(x1,x2)+1):
                    self.lights[i][j] = True
                
        if c == "turn off" or c == "turn off ":
            for i in range(min(y1, y2), max(y1, y2)+1):
                for j in range(min(x1,x2),max(x1,x2)+1):
                    self.lights[i][j] = False
                      
        if c == "switch" or c == "switch ":
            for i in range(min(y1, y2), max(y1, y2)+1):
                for j in range(min(x1,x2), max(x1,x2)+1):
                    self.lights[i][j] = not self.lights[i][j]
                    
    def count(self): 
        lightcounter = 0                                  
        for i in self.lights:
            
            '''count the number of coordinates that are True
            note: this is a multidimensional set up,
            thought process was - square multiplication table from
            programming '''
            
            for j in i:
                if j == True:
                    lightcounter +=1
        return lightcounter
        
        
def parseFile(file): 
    
    #checking if the input added starts with http
    #if it does, use requests.
    
    if file.startswith('http'):
        file1 = requests.get(file)
        file1 = file1.text.split('\n')
        
        for line in file1[:1]:
            print("the size is", line)
            length = int(line)
            switchboard = lightTest(length)
            for line in file1[1:-1]:
            
                find = pat.match(line)
                if find:
                    command = find.group(1)
                    x1 = find.group(2)
                    y1 = find.group(3)
                    x2 = find.group(4)
                    y2 = find.group(5)
                    switchboard.command(command, int(x1), int(y1), int(x2), int(y2))
        print("The number of lights left on are", switchboard.count())
        
    else:
        
        #else, use the local files.
   
        file1  = open(file, 'r')
        file1 = file1.readlines()   
        for line in file1[:1]:
            print("the size is", line)
            length = int(line)
            switchboard = lightTest(length)
            for line in file1[1:]:
                find = pat.match(line)
                if find:
                    command = find.group(1)
                    x1 = find.group(2)
                    y1 = find.group(3)
                    x2 = find.group(4)
                    y2 = find.group(5)
                    switchboard.command(command, int(x1), int(y1), int(x2), int(y2))
        print("The number of lights left on are", switchboard.count())
     
     
 
            
  
        
        
       





