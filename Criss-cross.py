from random import random
from tkinter import *
import tkinter as tk
import random
import tkinter.messagebox as mb
window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('380x375')
window.resizable(width=False, height=False)
game = [None] * 9
game_left = list(range(9))
def push(a):
    global game
    global game_left
    game[a] = 'X'
    buttons[a].config(text = 'X', font= ('Verdana', 13, 'bold'), bg="yellow", state = 'disable')
    game_left.remove(a)
    if check_win('X'):
        msg = "Вы победили!"
        mb.showinfo("Game Over", msg)
    else:
        if (len(game_left) > 1):
            t = random.choice(game_left)
            game[t] = 'O'
            buttons[t].config(text = 'O', state = 'disable')
            game_left.remove(t)
            if check_win('O'):
                msg = "Вы проиграли!"
                mb.showinfo("Game Over", msg)
        else:
            msg = "Игра окончена!"
            mb.showinfo("Game Over", msg)
def check_win(n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or (game[3] == n and game[4] == n and game[5] == n) or (game[6] == n and game[7] == n and game[8] == n)\
        or (game[0] == n and game[3] == n and game[6] == n) or (game[1] == n and game[4] == n and game[7] == n) or (game[2] == n and game[5] == n and game[8] == n)\
        or (game[0] == n and game[4] == n and game[8] == n) or (game[2] == n and game[4] == n and game[6] == n):
        return True
buttons = [Button(width=10, height=7, bg='blue', command=lambda x=i: push(x)) for i in range(9)]
row =1; col =0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col +=1
    if col == 3:
        row +=1
        col = 0
window.mainloop()