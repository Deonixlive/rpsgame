#We construct a markov chain 2nd order.

"""order 2 transition matrix looks like this:
    
               
               RR RP RS PR PP PS SR SP SS
Rock         [[0, 0, 0, 0, 0, 0, 0, 0, 0],
Paper         [0, 0, 0, 0, 0, 0, 0, 0, 0],
Scissors      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

"""
import itertools
import numpy as np
import random

#bulding blocks of all states, R = rock, P = paper, S = scissor
states = ["R","P","S"]

class Mc():   
    def __init__(self, order):
        
        #set a few variables and create a transition matrix filled with zeros and alls possible states
        self.tmatrix = [[],[],[]]
        self.correspond = {}
        self.state = []
        self.order = order
        for i in range(3**order):
            self.tmatrix[0].append(0)
            self.tmatrix[1].append(0)
            self.tmatrix[2].append(0)     
            
        #the size of the index matches the number of all possible states
        self.index = list(itertools.product(states, repeat=order))
        
    def predict(self):
#create a single column from the transition matrix dependend on the current state in self.state  
        istherezero = 0       
        if len(self.state) < self.order:
            #print("DEBUG 1")            
            return random.choice(states)[0]
            pass
    
#if there are 3 zeros, we should use random.choice() instead of random.choices()
        #print("DEBUG 1")
        j = self.row_finder()
        column = [float(self.tmatrix[0][j]),float(self.tmatrix[1][j]),float(self.tmatrix[2][j])]        
        #print(str(j))
        #print(column)
        for ele in column:
            if ele != 0:
                pass
            else:
                istherezero +=1 
        #print(istherezero)
        if istherezero == 3:
            #print("DEBUG 3")
            return random.choices(states)[0]
        
#bit of code that returns a choice according with a probability proportional to the weights in the transition matrix
        for j in range(len(self.index)):
            if self.state == list(self.index[j]):
                #print("DEBUG 2")
                return random.choices(states, weights=column)[0]

#turn the prediction into an actual pick          
    def pick(self):        
        predi = self.predict()
        if predi == "R":
            return "P"
        elif predi == "P":
            return "S"
        elif predi == "S":
            return "R"

#Searches a row which suits the current state. return None if it finds nothing
    def row_finder(self):
        for o in range(len(self.index)):
            if self.state == list(self.index[o]):
                return o
            
#bit of code that improves the mc
    def update(self, plg):
#ignore the first m rounds
        pos = self.row_finder()
        if len(self.state) < self.order:
            pass
        else:
            if plg == "R":
                self.tmatrix[0][pos] += 1
            elif plg == "P":
                self.tmatrix[1][pos] += 1
            elif plg == "S":
                self.tmatrix[2][pos] += 1
        self._state_updater(plg) 
        
#updating state after a round        
    def _state_updater(self, plg):
#adding state in the first m rounds
        if len(self.state) < self.order:
            self.state.append(plg)
        else:
            for it in range(0,self.order-1):
                self.state[it] = self.state[it+1]
            self.state[self.order-1] = plg

            
            
            
#First takes in the player choice than the AI's    
def winner(playerg, aig):
#deciding who wins, takes "R","P" or "S" as the choice of both players as input
    if type(playerg)!=type("") or type(aig)!=type(""):
        print("Error! type not str!")
       
    if playerg == aig:
        return "3"
    elif (playerg == "R" and aig=="S") or (playerg=="P" and aig=="R") or (playerg=="S" and aig=="P"):
        return "2"
    else:
        return "1"
    
    



"""
The selector creates an x number of Mc's and selects them.
The chart with the results looks like this:

The column refers to the n-th round, while the row refers to the ai.

round  1  2  3  4  5
ai1 [[ 1  0  1  -1  1]
ai2  [ 0  0  0  -1  0]
ai3  [-1  0  1   1  0]   
...

central are the functions .update(playerpick) and .turn() which returns the best pick according to their past score. 
"""
class Selector():
    def __init__(self, focus=5, numbai=5):
        self.focl = focus
        self.numai = numbai
        self.chart = []
        self.ai = []
        self.rounds = 0
#create ai's chart     
        for x in range(0,self.numai):
            self.chart.append([])
            self.ai.append(Mc(x+1))
            
#Update states, matrices and calculate score.            
    def update(self, plg):
        self.rounds += 1
        for x in range(self.numai):
#update via Mc update function
            self.ai[x].update(plg)  
            result = winner(self.ai[x].pick(), plg)
#if AI wins, add 1 to chart, looses add -1 and if theres a tie, add 0.
            if result == "1":
                self.chart[x].append(1)
            elif result == "2":
                self.chart[x].append(-1)
            elif result == "3":
                self.chart[x].append(0)
                
#pickes the AI which had the most score in the last f(focus) rounds. Uses the f newst scores from each AI in the chart     
    def pickai(self):
#calculating sums        
        self.sums = {}
        for x in range(self.numai):
            self.sums[str(x)] = 0
            if self.focl > self.rounds:
                for element in self.chart[x]:
                    self.sums[str(x)] += element
            else:
                for y in range(self.focl):
                    self.sums[str(x)] += self.chart[x][self.rounds-1-y]
#getting the highest scores
        highest_key = 0
        for key, value in self.sums.items():
            if value > self.sums[key]:
                highest_key = key
        return highest_key

#Make a pick based on .pickai()
    def turn(self):
        return self.ai[self.pickai()].pick()