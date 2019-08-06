
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

                
        print(self.player2_moves.append(pos)) 



        s = State(self.board) 
        s.children() 

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

    while True: 
        try: 
            if g.isComplete(): 
                break 

            print("Player 1 turn, enter a number in range (0-9)") 
            p1_move = int(input()) 
            g.move(p1_move, p1) 
            g.print() # print board 

            if g.winner()[0]: 
                print("Player 1 WON!", g.winner()[0]) 
                break 

            print("Player 2 turn, enter a number in range (0-9)") 
            p2_move = int(input()) 
            g.move(p2_move,p2) 
            g.print() 

            if g.winner()[0]: 
                print("Player 2 WON!") 
                break 

            if p1_move > 9 or p2_move > 9: 
                raise ValueError("Invalid Move") 
                

        except ValueError: 
            print("invalid input") 



if __name__ == '__main__': 
    main() 




