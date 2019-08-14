from math import inf 
from copy import deepcopy 
                
class Node(object): 
    def __init__(self, board, local):
        self.board = board
        self.child = None
        self.local = local
        self.depth = 0
        self.score = -inf # 10 win, -10 loose, 0 tie

        self.terminal_node = False
    def isComplete(self):
        '''          
            return true if board is a terminal 
        '''          
        for r in range(3):
            for c in range(3):
                if type(self.board[r][c]) == int:
                    return False
        return True  
             
    def prnt(self, brd): 
        print("_"*10) 
        for row in range(3): 
            for col in range(3): 
                print(brd[row][col], ' ',  flush=True, end='') 
            print('\n') 
        print("_"*10) 

    def openspots(node): 
        children = 0 
        node.local = dict() 
        for row in range(3):
            for col in range(3):
                elmnt = node.board[row][col]
                if type(elmnt) == int: 
                    node.local[elmnt] = (row,col) 
        
        return node.local  
           
    def create_child(node, turn):
        num_children = len(node.openspots()) 
        node.num = num_children
        child = [0 for _ in range(num_children) ]  # store nodes of children nodes
        boards = [0 for _ in range(num_children)]
        idx = 0 
        
        for k in node.local.keys(): 
            row = node.local[k][0] 
            col = node.local[k][1] 
            tmp_board = deepcopy(node.board)
        
            if turn == 'X': 
                if node.winner()[0] == False or node.isComplete() == False : # if winner is found or board is complete don't produce more child nodes 
                    tmp_board[row][col] = 'X' 
        
            else: 
                if node.winner()[0] == False or node.isComplete() == False : # if winner is found or board is complete don't produce more child nodes 
                    tmp_board[row][col] = 'O' 
                    
            boards[idx] = tmp_board
        
            child[idx] = Node(tmp_board, num_children) 
            child[idx].set_score() 
                
            idx += 1 
            node.depth+= 1 
        
        node.child = child 
        return child            

    def set_score(self): 
        if self.winner()[0]: 
            if self.winner()[1] == {'O'}: 
                self.score = 10 # win 
            elif self.winner()[1] == {'X'}: 
                self.score = -10 # loss  
                      
        if self.isComplete(): 
            if not self.winner()[0]: 
                self.score = 0 # draw 

                        
    def winner(self): 
        for row in self.board: 
            if len(set(row)) == 3:  
                continue 
            elif len(set(row)) == 1:  
                return (True, set(row)) 
            
        diag_1 = (self.board[0][0], self.board[1][0], self.board[2][0]) 
        if len(set(diag_1)) == 1:  
            return (True, set(diag_1)) 
            
        diag_2 = (self.board[0][0], self.board[1][0], self.board[2][0]) 
        if len(set(diag_2)) == 1:  
            return (True, set(diag_2)) 
            
        diag_3 = (self.board[0][0], self.board[1][1], self.board[2][2])
        if len(set(diag_3)) == 1:  
            return (True, set(diag_3)) 
            
        diag_4 = (self.board[0][1], self.board[1][1], self.board[2][1])
        if len(set(diag_4)) == 1:  
            return (True, set(diag_4)) 
            
        diag_5 = (self.board[0][2], self.board[1][2], self.board[2][2])
        if len(set(diag_5)) == 1:  
            return (True, set(diag_5)) 
            
        diag_6 = (self.board[2][0], self.board[1][1], self.board[0][2])
        if len(set(diag_6)) == 1:  
            return (True, set(diag_6)) 
            
        return (False, None)
 

    def minimax(self, depth, maximizingPlayer):
        if depth == 0 or self.isComplete():
            return self.score

        if maximizingPlayer:
            value = inf
            for c in self.child:
                value = max(value, minimax(c, depth -1, False))
            return value

        else: # minimizing player
            value = -inf
            for c in self.child:
                value = min(value, minimax(c, depth -1, True))
            return value
