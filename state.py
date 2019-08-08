from game import Game 
from tree import Node 
class State(Game): 

    def __init__(self, currentState): 
        self.possible_moves = list() 
        self.currentState = currentState 
        self.count = 0 # count open spots (for generating # of nodes)    

    def children(self, maxiPlayer): 
        count = 0 
        for row in range(3): 
            for col in range(3): 
                if type(self.currentState[row][col])  == int: 
                    pairs = (row, col)
                    self.possible_moves.append(pairs) 
                    count += 1 
            
        self.node = Node(self.currentState, self.possible_moves) 

        if maxiPlayer == 'O': 
            self.node.create_child('O') 
            self.count = count 

        else: 
            self.node.create_child('X') 
            self.count = count 
            

        return self.count 
