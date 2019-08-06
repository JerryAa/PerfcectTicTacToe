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
                        
