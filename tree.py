

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

def main(): 
    brd = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    count = 0 

    for row in range(3): 
        for col in range(3): 
            brd[row][col] = count 
            count += 1 

    brd[1][2] = 'X' 

    locations = list() 
    children = 0 

    for row in range(3): 
        for col in range(3): 
            if type(brd[row][col]) == int: 
                pairs = (row, col) 
                locations.append(pairs) 
                children += 1 

    n = Node(brd, locations) 
    n.create_child(children) 

if __name__ == '__main__': 
    main() 
