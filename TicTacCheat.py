import tkinter as tk


class BuildBoard(object):
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('Tic Tac CheatSheet')
        self.root.geometry('900x900')
        self.root.config(bg='white') 

        self.gridTo2D = dict()

        self.save_turn = list() 
        self.turn = tk.LabelFrame(self.root, text='Turn', bg='cyan2', font=("Times bold", 60))
        self.turn.grid(row=10, column=26)

        self.whose_turn = tk.IntVar()
        self.o_turn = tk.Radiobutton(
            self.turn, state='disabled', text='O', variable=self.whose_turn, value=1, bg='red3', font=("Times", 20))
        self.o_turn.select()
        self.o_turn.grid(row=6, column=12)


        self.x_turn = tk.Radiobutton(
            self.turn, state='disabled', text='X', variable=self.whose_turn, value=0, bg ='medium blue', font=("Times", 20)) 
        self.x_turn.deselect()
        self.x_turn.grid(row=5, column=12)


        self.button = list() 

        self.build_grid()

        self.close = tk.Button(self.root, text='Close', command=self.root.quit)
        self.solve = tk.Button(self.root, text='Solve',
                               command=self.solve_button)
        self.reset = tk.Button(self.root, text='Reset',
                               command=self.reset_button)

        self.close.place(relx=0.6, rely=0.5, anchor='w')
        self.solve.place(relx=0.7, rely=0.5, anchor='w')
        self.reset.place(relx=0.8, rely=0.5, anchor='w')

        self.root.mainloop()

         
    def build_grid(self):
        count = 0
        for r in range(3):
            for c in range(3):
                self.button.append(tk.Button(self.root, font=('courier', 10), text=str(
                count), width=10, height=5, command=lambda e=count: self.click(e))) 

                self.button[count].grid(row=r, column=c)
                    
                self.gridTo2D[count] = [(r, c)]

                count += 1

    def click(self, value=None):

        # print(f'Button number {value}') 

        self.photo_x = tk.PhotoImage(file="X.png")
        self.photo_o = tk.PhotoImage(file="O.png")

        if self.whose_turn.get() == 0:  # x's turn
            self.save_turn.append(('X', value)) 
            self.button[value].config(bg="medium blue") 
            self.button[value].config(state="disabled") 
            self.x_turn.deselect()
            self.o_turn.select()

        else:  #  o's turn
            self.save_turn.append(('O', value)) 
            self.button[value].config(bg="Red3") 
            self.button[value].config(state="disabled") 
            self.o_turn.deselect()
            self.x_turn.select()

    def solve_button(self):
        win = tk.Toplevel(self.root)
        win.geometry('900x900')
        label = tk.Label(win, text='Solve window', fg='SlateBlue1',  font=("Rockwell bold", 30)) 

        win.config(bg='white')

        canvas = tk.Canvas(win, width=900, height=900)
        canvas.config(bg='white')
        canvas.pack()


        x = 40
        y = 40
        square = {'x': x, 'y':y, 'width':432 + x, 'length':432 + y}  
         
        quad_len = square['length'] - y 
        quad_len /= 3 
         
        quadrants = [None]*9
        font_size = 70
         
        quadrants[0] = (square['x']+ (quad_len//2), font_size ) 
        quadrants[1] = (quad_len + quadrants[0][0] , font_size )
        quadrants[2] = (quad_len + quadrants[1][0] , font_size )
        quadrants[3] = (quadrants[0][0] , font_size + 100 )
        quadrants[4] = (quadrants[3][0] + quad_len , font_size + 100 )
        quadrants[5] = (quadrants[4][0] + quad_len , font_size + 100 )
        quadrants[6] = (quadrants[0][0] , font_size + 200)
        quadrants[7] = (quadrants[6][0] + quad_len, font_size + 200)
        quadrants[8] = (quadrants[7][0] + quad_len, font_size + 200)
         
        ''' 
        canvas.create_text(quadrants[0], text='X', fill='blue', font=('times bold', font_size)) 
        canvas.create_text(quadrants[1], text='O', fill='red', font=('times bold', font_size)) 
        canvas.create_text(quadrants[2], text='X', fill='blue', font=('times bold', font_size)) 
        canvas.create_text(quadrants[3], text='O', fill='red', font=('times bold', font_size)) 
        canvas.create_text(quadrants[4], text='X', fill='blue', font=('times bold', font_size)) 
        canvas.create_text(quadrants[5], text='O', fill='red', font=('times bold', font_size)) 
        canvas.create_text(quadrants[6], text='X', fill='blue', font=('times bold', font_size)) 
        canvas.create_text(quadrants[7], text='O', fill='red', font=('times bold', font_size)) 
        canvas.create_text(quadrants[8], text='X', fill='blue', font=('times bold', font_size)) 
        ''' 
         
         
        canvas.create_rectangle(square['x'], square['y'], square['width'], square['length'], state='disabled') 
         
        canvas.create_line(quad_len + square['x'] , square['x'], quad_len + square['x'], square['length'], fill="black", width=4) # line 1
        canvas.create_line(quad_len * 2 + square['x'] , square['x'], quad_len * 2 + square['x'], square['length'], fill="black", width=4) # line 2
        canvas.create_line(square['x'], quad_len + square['y'] , square['width'], quad_len + square['y'], fill="black", width=4)  # line 3 
        canvas.create_line(square['x'], quad_len * 2 + square['y'] , square['width'], quad_len * 2 + square['y'], fill="black", width=4)  # line 4 
         

        win.mainloop()


    def reset_button(self):
        new_root = tk.Tk()
        del self.root
        self.root = new_root 

