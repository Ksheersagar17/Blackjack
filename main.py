from tkinter import *
from PIL import ImageTk,Image
import gamePage, main_code

def goin(root):
    main_code.start()
    # root.destroy()
    # gamePage.gameUI()
    
def goout(root):
    root.destroy()

def gameon():
    root = Tk()
    root.resizable(width= False, height= False)
    WW = 750
    WH = 400
    SW = root.winfo_screenwidth()
    SH = root.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    root.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    root.title('Blackjack')
    root.config(bg='green')

    ic = Image.open('assets/logo.png')
    res_img = ic.resize((400,300))

    canvas = Canvas(root, bg="green", width=900, height=500)
    canvas.place(x=0, y=0)

    photoimage = ImageTk.PhotoImage(res_img)
    canvas.create_image(250, 200, image=photoimage)

    b1 = Button(root, text='Start', font=(40), height=1, width=15, command= lambda : goin(root))
    b2 = Button(root, text='Exit', font=(40), height=1, width=15, command = lambda : goout(root))

    b1.place(x=530, y=120)
    b2.place(x=530, y=190)

    root.mainloop()