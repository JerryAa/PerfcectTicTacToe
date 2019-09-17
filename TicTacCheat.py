import tkinter as tk


class BuildBoard(object):
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('Tic Tac CheatSheet')
        self.root.geometry('900x900')

        self.gridTo2D = dict()

        self.turn = tk.LabelFrame(self.root, text='Turn', font=("Times bold", 60))
        self.turn.grid(row=5, column=16)

        self.whose_turn = tk.IntVar()

        self.x_turn = tk.Radiobutton(
            self.turn, state='disabled', text='X', variable=self.whose_turn, value=0, bg ='blue', font=("Times", 16)) 
        self.x_turn.select()
        self.x_turn.grid(row=5, column=12)

        self.o_turn = tk.Radiobutton(
            self.turn, state='disabled', text='O', variable=self.whose_turn, value=1, bg='red', font=("Times", 16))
        self.o_turn.deselect()
        self.o_turn.grid(row=6, column=12)


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
        print(f'Button number {value}') 
        self.photo_x = tk.PhotoImage(file="X.png")
        self.photo_o = tk.PhotoImage(file="O.png")

        if self.whose_turn.get() == 0:  # x's turn
            self.button[value].config(bg="blue") 
            self.button[value].config(state="disabled") 
            self.x_turn.deselect()
            self.o_turn.select()
        else:  # 1 o's turn
            self.button[value].config(bg="Red") 
            self.button[value].config(state="disabled") 
            self.o_turn.deselect()
            self.x_turn.select()

    def solve_button(self):
        win = tk.Toplevel(self.root)
        win.geometry('900x900')
        label = tk.Label(win, text='Solve window')
        label.pack()

    def reset_button(self):
        new_root = tk.Tk()
        del self.root
        self.root = new_root
        self.build_grid()


def main():
    board = BuildBoard()


if __name__ == '__main__':
    main()
