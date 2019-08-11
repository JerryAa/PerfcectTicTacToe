
# goal is to implement min-max so that computer is unbeatable 

from tree import Node 
from game import Game 
from state import State 
from copy import deepcopy                                                                                                                                               
class Player(Game): 
    def __init__(self, p1 ,p2): 
        self.player1 = p1 
        self.player2 = p2 
        super().__init__(self.player1, self.player2)
        self.player1_moves = list() 
        self.player2_moves = list()  

    def move(self,pos, player): 
        def update(position, player): 
            row = self.num_2dlist[position][0] 
            col = self.num_2dlist[position][1] 
            
            if player == self.player1: 
                self.board[row][col] = 'X'
            else: 
                self.board[row][col] = 'O'

        if player == self.player1 or player == self.player2: 
            update(pos, player) 
            
            if player == self.player1: 
                self.player1_moves.append(pos) 
            else: 
                self.player2_moves.append(pos) 

                
        self.player2_moves.append(pos)  

        s = State(self.board) 
        s.children('O') # maxPlayer
        
        
# raise ValueError("MOVE already made") 

    def isComplete(self): 
        ''' 
            check if board is complete 
        '''
        for r in range(3):  
            for c in range(3):  
                if type(self.board[r][c]) == int:
                    return False 

            
        return True  

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


def main(): 
    ''' 
    p1 = input("Enter Player 1 name: ") 
    p2 = input("Enter Player 2 name: ") 


    if p1 == p2: 
        raise NameError ("NAMES ARE THE SAME")

    if (len(p2) == 0): 
        p2 = "Computer" 

    ''' 
    p1 = 'a'
    p2 = 'b'

    g = Player(p1, p2) 
    g.print() # print inital board 
    mvs = 9 # total number of moves that can be made 

    while True: 
        try: 
            p1_move = int(input("Player 1 turn, enter a number in range (0-9): ") )
            if p1_move > 9 or p1_move < 0: 
                raise Exception("Invalid Move!") 
                
            g.move(p1_move, p1) 
            g.print() # print board 

            if g.winner()[0]: 
                print("Player 1 WON!") 
                break 

            if g.isComplete(): 
                print("DRAW") 
                break 

            p2_move = int(input("Player 2 turn, enter a number in range (0-9): ")) 
            if p2_move > 9 or p2_move < 0: 
                raise Exception("Invalid Move!") 
                
            g.move(p2_move,p2) 
            g.print() 

            if g.winner()[0]: 
                print("Player 2 WON!") 
                break 

            if g.isComplete(): 
                print("DRAW") 
                break 


        except ValueError: 
            print("invalid input") 



if __name__ == '__main__': 
    main() 




