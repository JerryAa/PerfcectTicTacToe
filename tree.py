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

             
    def prnt(self, brd): 
        print("_"*10) 
        for row in range(3): 
            for col in range(3): 
                print(brd[row][col], ' ',  flush=True, end='') 
            print('\n') 
        print("_"*10) 
                
    def create_child(node, num_children):
        child = [0 for _ in range(num_children) ]  # store nodes of children nodes
        boards = [0 for _ in range(num_children)]
 
        for i in range(0, len(node.local)):
            tmp_board = deepcopy(node.board)
            row = node.local[i][0]
            col = node.local[i][1]
 
            tmp_board[row][col] = 'O' 
            boards[i] = tmp_board
            child[i] = Node(tmp_board, num_children)
                
            if child[i].winner()[0]: 
                if child[i].winner()[0] and child[i].winner()[1] == 'O': 
                    child[i].score = 10  
                elif child[i].winner()[0] and child[i].winner()[1] == 'X': 
                    child[i].score = -10 
                else: 
                    child[i].score = 0 
                        
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
 

