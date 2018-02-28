'''
Created on 28 Feb 2018

@author: mary-katetyrrell
'''

class lightTest():
    
    lights = None
    '''
    this class will test the number of lights that are left on
    
    '''
    def __init__(self, size):
        
        '''initialise the multidimensional array, to the size of the input'''
        
        self.size = size
        self.lights = [[False]*size for _ in range(size)]
        
    def command(self, c, x1, y1, x2, y2):
        
        '''Take in the parsed variables and use them accordingly'''
    
        self.c = c  #corresponds to group1
        self.x1 = x1    #corresponds to group2
        self.y1 = y1    #corresponds to group3
        self.x2 = x2    #corresponds to group4
        self.y2 = y2    #corresponds to group5
        
        '''check the nature of the commands and adjust the cordinates as so'''
        
        if c == "turn on":
            
            for i in range(x1,x2):
                for j in range(y1, y2):
                    self.lights[i][j] = True
                
        if c == "turn off":
            for i in range(x1,x2):
                for j in range(y1, y2):
                    self.lights[i][j] = False
                      
        if c == "switch":
            for i in range(x1,x2):
                for j in range(y1, y2):
                    if self.lights[i][j] == True:
                        self.lights[i][j] = False
                    if self.lights[i][j] == False:
                        self.lights[i][j] = True
                
        def light_count(self):
            for i in self.lights:
                lightcounter = 0
                for j in i:
                    if j == "True":
                        lightcounter +=1
            return lightcounter
                
            
                        
                 
            
       
         
           







    

       
