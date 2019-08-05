

from copy import deepcopy 

class Node(object): 
    def __init__(self, board, local):
        self.board = board 
        self.child = None 
        self.local = local  


    def prnt(self, brd): 
        print("_"*20) 
        for row in range(3): 
            for col in range(3): 
                print(brd[row][col], ' ',  flush=True, end='') 
            print('\n') 
        print("_"*20) 

    def create_child(node, num_children): 
        boards = [0]*num_children 
        for i in range(0, len(node.local)):  
            tmp_board = deepcopy(node.board) 
            row = node.local[i][0] 
            col = node.local[i][1] 

            tmp_board[row][col] = 'O' 
            boards[i] = tmp_board 


            node.prnt(tmp_board) 
            node.child = Node(node.board, num_children) 


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
# NODE_LIST / NODE ARRAY 
    n.create_child(children) 

if __name__ == '__main__': 
    main() 
