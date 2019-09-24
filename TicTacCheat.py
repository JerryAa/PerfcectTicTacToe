import tkinter as tk


class BuildBoard(object):
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('Tic Tac CheatSheet')
        self.root.geometry('900x900')
        self.root.config(bg='white')

        self.gridTo2D = {0: [(0, 0)], 1: [(0, 1)], 2: [(0, 2)], 3: [(1, 0)], 4: [(1, 1)], 5: [(1, 2)], 6: [(2, 0)], 7: [(2, 1)], 8: [(2, 2)]}

        self.frame = tk.Frame(self.root, width=200, height = 600)
        self.frame.pack(side='bottom', fill='x', padx=10,pady=10)


        self.save_turn = list()
        self.turn = tk.LabelFrame(
            self.frame, text='Turn', bg='cyan2', font=("Times bold", 60))
# self.turn.grid(row=10, column=26)

        self.whose_turn = tk.IntVar()
        self.o_turn = tk.Radiobutton(
            self.turn, state='disabled', text='O', variable=self.whose_turn, value=1, bg='red3', font=("Times", 20))
        self.o_turn.select()
# self.o_turn.grid(row=6, column=12)

        self.x_turn = tk.Radiobutton(
            self.turn, state='disabled', text='X', variable=self.whose_turn, value=0, bg='medium blue', font=("Times", 20))
        self.x_turn.deselect()
# self.x_turn.grid(row=5, column=12)

        self.button = list()

        self.build_grid()
        self.setup_buttons()
        self.root.mainloop()

    def build_grid(self):

        self.canvas = tk.Canvas(self.frame, width=900, height=900)
        self.canvas.config(bg='white')

        x = 0
        y = 0
        square = {'x': x, 'y': y, 'width': 99 + x, 'length': 99 + y}

        quad_len = square['length'] - y
        quad_len /= 3

        quadrant = [None]*9  # coordinates for each quadrant
        q = [None]*9  # x,y pairs

        font_size = int(quad_len/2)

        self.canvas.create_rectangle(square['x'], square['y'], square['width'], square['length'], state='disabled')
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)

        colors = [ 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2', 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue']


        from random import shuffle
        shuffle(colors)
        print('\n')

        self.rectangle = list()
        idx = 0

        for row in range(x, square['length'], int(quad_len)):
            for col in range(x, square['width'] , int(quad_len)):
                coords = (col, row,quad_len + col, quad_len + row )
                self.rectangle.append(self.canvas.create_rectangle(coords,  fill=colors[idx], state='normal')) 
                self.canvas.tag_bind(self.rectangle[idx], "<Button>", lambda item=self.rectangle[idx], index=idx : self.click(item, index)) 
                idx += 1


    def click(self, iD=None,value =None): 
# print(iD, value) 
        
        if self.whose_turn.get() == 0:  # x's turn
            self.save_turn.append(('X', value))
            self.canvas.itemconfig(self.rectangle[value], fill="medium blue", state='disabled') 
            self.x_turn.deselect()
            self.o_turn.select()

        else:  # o's turn
            self.save_turn.append(('O', value))
            self.canvas.itemconfig(self.rectangle[value], fill="Red3", state='disabled') 
            self.o_turn.deselect()
            self.x_turn.select()

    def solve_button(self):
        win = tk.Toplevel(self.root)
        win.geometry('900x900')
        label = tk.Label(win, text='Solve window',
                         fg='SlateBlue1',  font=("Rockwell bold", 30))

        win.config(bg='white')

        canvas = tk.Canvas(win, width=900, height=900)
        canvas.config(bg='white')
        # id = C.create_line ( x0, y0, x1, y1, ..., xn, yn, option, ... )
        x = 0
        y = 0
        square = {'x': x, 'y': y, 'width': 60 + x, 'length': 60 + y}

        quad_len = square['length'] - y
        quad_len /= 3

        quadrant = [None]*9  # coordinates for each quadrant
        q = [None]*9  # x,y pairs

        font_size = int(quad_len/2)

        quadrant[0] = (square['x'] + (quad_len//2), font_size)

        canvas.create_rectangle(
            square['x'], square['y'], square['width'], square['length'], state='disabled')

        canvas.create_line(quad_len + square['x'], square['x'], quad_len +
                           square['x'], square['length'], fill="black", width=4)  # line 1
        canvas.create_line(quad_len * 2 + square['x'], square['x'], quad_len *
                           2 + square['x'], square['length'], fill="black", width=4)  # line 2
        canvas.create_line(square['x'], quad_len + square['y'], square['width'],
                           quad_len + square['y'], fill="black", width=4)  # line 3
        canvas.create_line(square['x'], quad_len * 2 + square['y'], square['width'],
                           quad_len * 2 + square['y'], fill="black", width=4)  # line 4

        quadrant[0] = (0, quad_len, quad_len, quad_len)
        q[0] = (quadrant[0][2] - font_size, quadrant[0][2] - font_size)
        quadrant[1] = (quad_len, quad_len, quad_len*2, quad_len)
        q[1] = (quadrant[1][2] - font_size, font_size)

        quadrant[2] = (quad_len*2, quad_len, quad_len*3, quad_len)
        q[2] = (quadrant[2][2] - font_size, font_size)

        quadrant[3] = (0, quad_len*2, quad_len, quad_len*2)
        q[3] = (quadrant[3][2] - font_size, quadrant[3][1] - font_size)

        quadrant[4] = (quad_len, quad_len*2, quad_len*2, quad_len*2)
        q[4] = (quadrant[4][2] - font_size, quadrant[4][2] - font_size)

        quadrant[5] = (quad_len*2, quad_len*2, quad_len*3, quad_len*2)
        q[5] = (quadrant[5][2] - font_size, quadrant[5][3] - font_size)

        quadrant[6] = (0, quad_len*3, quad_len, quad_len*3)
        q[6] = (quadrant[6][2] - font_size, quadrant[6][3] - font_size)

        quadrant[7] = (quad_len, quad_len*3, quad_len*2, quad_len*3)
        q[7] = (quadrant[7][2] - font_size, quadrant[7][3] - font_size)

        quadrant[8] = (quad_len*2, quad_len*3, quad_len*3, quad_len*3)
        q[8] = (quadrant[8][2] - font_size, quadrant[8][2] - font_size)

        for choice in self.save_turn:
            if choice[0] == 'X':
                canvas.create_text(q[choice[1]],  text='X',
                                   fill='blue', font=('times bold', font_size))
            else:
                canvas.create_text(q[choice[1]],  text='O',
                                   fill='red', font=('times bold', font_size))

        canvas.pack() 

        win.mainloop()

    def setup_buttons(self):

        self.close = tk.Button(self.frame, text='Close', command=self.frame.quit)

        self.solve = tk.Button(self.frame, text='Solve',
                               command=self.solve_button)

        self.reset = tk.Button(self.frame, text='Reset',
                               command=self.reset_button) 

        self.close.pack(side=tk.BOTTOM, anchor=tk.CENTER) 
        self.solve.pack(side=tk.BOTTOM, anchor=tk.CENTER) 
        self.reset.pack(side=tk.BOTTOM, anchor=tk.CENTER) 


# self.frame.pack(side=tk.BOTTOM) 

    def reset_button(self):
        self.root.destroy() 
        new_root = tk.Tk()
        self.root = new_root

    
