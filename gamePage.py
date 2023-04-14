from tkinter import *
from PIL import ImageTk,Image

def gameUI():
    gp = Tk()

    # gp.resizable(width= False, height= False)
    WW = 750
    WH = 400
    SW = gp.winfo_screenwidth()
    SH = gp.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    gp.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    gp.title('Blackjack')
    gp.config(bg='green')

    ic1 = Image.open('assets/dealer.png')
    res_img1 = ic1.resize((100,100))
    canvas1 = Canvas(gp, bg="green", width=120, height=120)
    canvas1.place(x=30, y=30)
    photoimage1 = ImageTk.PhotoImage(res_img1)
    canvas1.create_image(60, 60, image=photoimage1)

    ic2 = Image.open('assets/man.png')
    res_img2 = ic2.resize((100,100))
    canvas2 = Canvas(gp, bg="green", width=120, height=120)
    canvas2.place(x=30, y=230)
    photoimage2 = ImageTk.PhotoImage(res_img2)
    canvas2.create_image(60, 60, image=photoimage2)

    
    
    playerfrm = Frame(gp)
    playerfrm.configure(background='green')
    playerfrm.place(x=200, y=235)
    
    lst = ['assets/Clubs/2.png', 'assets/Hearts/A.png', 'assets/Spade/5.png']
    lab_lst = [0]*5
    pc=[0]*5
    r = 0
    for i in lst:
        pc[r] = Image.open(i)
        pc_res_img1 = pc[r].resize((80,100))
        pc[r] = ImageTk.PhotoImage(pc_res_img1)
        lab_lst[r] = Label(playerfrm, image=pc[r])
        lab_lst[r].grid(column=r,row=0)
        r = r+1
    
    # pc1 = Image.open('assets/Clubs/A.png')
    # pc_res_img1 = pc1.resize((80,100))
    # pc_canvas1 = Canvas(playerfrm, bg="white", width=75, height=95)
    # pc_canvas1.pack(padx=10, pady=10, side=LEFT)
    # pc_photoimage1 = ImageTk.PhotoImage(pc_res_img1)
    # pc_canvas1.create_image(40, 50, image=pc_photoimage1)

    # pc2 = Image.open('assets/Clubs/A.png')
    # pc_res_img2 = pc2.resize((80,100))
    # pc_canvas2 = Canvas(playerfrm, bg="white", width=75, height=95)
    # pc_canvas2.pack(padx=10, pady=10, side=LEFT)
    # pc_photoimage2 = ImageTk.PhotoImage(pc_res_img2)
    # pc_canvas2.create_image(40, 50, image=pc_photoimage2)

    gp.mainloop()

gameUI()
