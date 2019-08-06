
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

