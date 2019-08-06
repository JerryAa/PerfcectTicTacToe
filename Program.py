
# goal is to implement min-max so that computer is unbeatable 



import tree 

class Game(object): 
    def __init__(self, player1, player2): 
        self.player1 = player1 
        self.player2 = player2 
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.num_2dlist = {0: [0,0], 
                           1: [0,1],
                           2: [0,2],
                           3: [1,0],
                           4: [1,1],
                           5: [1,2],
                           6: [2,0],
                           7: [2,1],
                           8: [2,2]}

        self.create_board() 

    def create_board(self): 
        count = 0 
        for x in range(3): 
            for y in range(3): 
                self.board[x][y] = count 
                count += 1 

    def print(self): 
        print("\n") 
        for x in range(3): 
            for y in range(3): 
                print(self.board[x][y], ' ', flush=True, end='')
            print('\n') 
        print("\n") 

class State(Game): 

    def __init__(self, currentState): 
        self.possible_moves = list() 
        self.currentState = currentState 
        self.count = 0 # count open spots (for generating # of nodes)    

    def children(self): 
        count = 0 
        for row in range(3): 
            for col in range(3): 
                if type(self.currentState[row][col])  == int: 
                    pairs = (row, col)
                    self.possible_moves.append(pairs) 
                    count += 1 
            
        self.node = Node(self.currentState, self.possible_moves) 
        self.node.create_child(count) 
        self.count = count 

        return self.count 
                
from copy import deepcopy                                                                                                                                               
                
class Node(object): 
    def __init__(self, board, local):
        self.board = board 
        self.child = None 
        self.local = local  
                
             
    def prnt(self, brd): 
        print("_"*10) 
        for row in range(3): 
            for col in range(3): 
                print(brd[row][col], ' ',  flush=True, end='') 
            print('\n') 
        print("_"*10) 
                
    def create_child(node, num_children): 
        '''  
            don't score until "Win" 
            if terminal_state(WIN) 
                score = 10 
                
            if terminal_state(LOSS) 
                score = -10 
                
            if terminal_state(DRAW) 
                score = 0 
        '''  
        child = [0 for _ in range (num_children)] # store nodes of children nodes 
        boards = [0 for _ in range (num_children)] 
                
        for i in range(0, len(node.local)):  
            tmp_board = deepcopy(node.board) 
            row = node.local[i][0] 
            col = node.local[i][1] 
                
            tmp_board[row][col] = 'O' 
            boards[i] = tmp_board 
            child[i] = Node(tmp_board, num_children) 
                
        for i in range(num_children): 
            node.prnt(child[i].board) 
                


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
        for r in range(3):  
            for c in range(3):  
                if self.board[r][c] == 'X' or self.board[r][c] == 'O': 
                    return False 

            
        return True  

    def winner(self): 
        if self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X':
            return True 
        elif self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O':
            return True 

        if self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X':
            return True 
        elif self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O':
            return True 

        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            return True 
        elif self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            return True 

        if self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X':
            return True 
        elif self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O':
            return True 

        if self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X':
            return True 
        elif self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O':
            return True 

        if self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X':
            return True 
        elif self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O':
            return True 

        if self.board[2][0] == 'X' and self.board[1][1] == 'X' and self.board[0][2] == 'X':
            return True 
        elif self.board[2][0] == 'O' and self.board[1][1] == 'O' and self.board[0][2] == 'O':
            return True 

        if self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X':
            return True 
        elif self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O':
            return True 

        return False  


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
            print("Player 1 turn, enter a number in range (0-9)") 
            p1_move = int(input()) 
            g.move(p1_move, p1) 
            g.print() # print board 

            if g.winner(): 
                print("Player 1 WON!") 
                break 

            print("Player 2 turn, enter a number in range (0-9)") 
            p2_move = int(input()) 
            g.move(p2_move,p2) 
            g.print() 

            if g.winner(): 
                print("Player 2 WON!") 
                break 

            if p1_move > 9 or p2_move > 9: 
                raise ValueError("Invalid Move") 
                


            if g.isComplete(): 
                break 
        except ValueError: 
            print("invalid input") 



if __name__ == '__main__': 
    main() 




