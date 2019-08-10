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
        node.local = list() 
        for row in range(3):
            for col in range(3):
                if type(node.board[row][col]) == int:
                    pairs = (row, col)
                    node.local.append(pairs)
                    children += 1

        return children 

    def create_child(node, maxPlayer):
        num_children = node.openspots()
        child = [0 for _ in range(num_children) ]  # store nodes of children nodes
        boards = [0 for _ in range(num_children)]
 
        for i in range(0, len(node.local)):
           
            tmp_board = deepcopy(node.board)
            row = node.local[i][0]
            col = node.local[i][1]
 
 
            if maxPlayer == 'O': 
                tmp_board[row][col] = 'O'
                boards[i] = tmp_board
                child[i] = Node(tmp_board, num_children)
 
            else: # 'X' 
                tmp_board[row][col] = 'X'
                boards[i] = tmp_board
                child[i] = Node(tmp_board, num_children)
 
                
            child[i].set_score() 
            node.depth += 1 
 
        return child 

    def set_score(self): 
        if self.winner()[0]: 
            if self.winner()[0] and self.winner()[1] == 'O': 
                self.score = 10 # win 
            elif self.winner()[0] and self.winner()[1] == 'X': 
                self.score = -10 # loss  
                      
        if self.isComplete(): 
            if not self.winner()[0]: 
                self.score = 0 # draw 

                        
    def winner(self): 
        if self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X':
            return (True, 'X')
        elif self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O':
            return (True, 'O')
 
        if self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X':
            return (True, 'X')
        elif self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O':
            return (True, 'O')
 
        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            return (True, 'X')
        elif self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            return (True, 'O')
 
        if self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X':
            return (True, 'X')
        elif self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O':
            return (True, 'O')
 
        if self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X':
            return (True, 'X')
        elif self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O':
            return (True, 'O')
 
        if self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X':
            return (True, 'X')
        elif self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O':
            return (True, 'O')
 
        if self.board[2][0] == 'X' and self.board[1][1] == 'X' and self.board[0][2] == 'X':
            return (True, 'X')
        elif self.board[2][0] == 'O' and self.board[1][1] == 'O' and self.board[0][2] == 'O':
            return (True, 'O')
 
        if self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X':
            return (True, 'X')
        elif self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O':
            return (True, 'O')
 
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
