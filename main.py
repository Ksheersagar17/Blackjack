from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.resizable(width= False, height= False)
WW = 600
WH = 400
SW = root.winfo_screenwidth()
SH = root.winfo_screenheight()
x = SW/2 - WW/2
y = SH/2 - WH/2
root.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
root.title('Blackjack')
root.config(bg='green')


l1 = Label(root, text='BlackJack', bg='green', font=('ROG Fonts', 30))
l1.place(x=160, y=10)

b1 = Button(root, text='Start', font=(40), height=1, width=15)
b2 = Button(root, text='Exit', font=(40), height=1, width=15)

b1.place(x=220, y=120)
b2.place(x=220, y=190)



root.mainloop()