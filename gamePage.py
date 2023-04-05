from tkinter import *
from PIL import ImageTk,Image

def gameUI():
    gp = Tk()

    gp.resizable(width= False, height= False)
    WW = 750
    WH = 400
    SW = gp.winfo_screenwidth()
    SH = gp.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    gp.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    gp.title('Blackjack')
    gp.config(bg='green')


    gp.mainloop()
    
gameUI()