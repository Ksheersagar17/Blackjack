from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import main_code, main

def result(player_hand, dealer_hand, gp):
    if dealer_hand.value > 21:
        messagebox.showinfo(message='Dealer Bust !!  PLAYER WINS')
        # dealer_busts(player_hand,dealer_hand,player_chips)
    elif player_hand.value > 21:
        messagebox.showinfo(message='DEALER WINS!  BUST PLAYER!!')
    elif player_hand.value > dealer_hand.value:
        messagebox.showinfo(message='PLAYER WINS !!')
        # player_wins(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value > player_hand.value:
        messagebox.showinfo(message='DEALER WINS !!')
        # dealer_wins(player_hand,dealer_hand,player_chips)
    else:
        messagebox.showinfo(message='Player and Dealer tie... PUSH!!')
        # push(player_hand,dealer_hand)
    
    gp.destroy()
    main.start()
    

def HIT(deck, hand, dealer_hand, gp):
    main_code.hit(deck, hand)
    main_code.show_some(hand, dealer_hand, gp)
    
    if hand.value <= 21:
        while dealer_hand.value < 17:
            main_code.hit(deck, dealer_hand)
    else:
        result(hand, dealer_hand, gp)
        
    
def STAND(player_hand, dealer_hand, deck, gp):
    print(player_hand.value)
    print(dealer_hand.value)
    if player_hand.value <= 21:
        if dealer_hand.value < 17:
            main_code.hit(deck, dealer_hand)
        
    main_code.show_all(player_hand, dealer_hand, gp)
    # result()
    
    # if player_hand.value <= 21:
        # while dealer_hand.value < 17:
    #         main_code.hit(deck,dealer_hand)
        
    #     main_code.show_all(player_hand,dealer_hand)
        
    #     if dealer_hand.value > 21:
    #         main_code.dealer_busts(player_hand,dealer_hand, main_code.player_chips)
    #     elif player_hand.value > dealer_hand.value:
    #         main_code.player_wins(player_hand,dealer_hand, main_code.player_chips)
    #     elif dealer_hand.value > player_hand.value:
    #         main_code.dealer_wins(player_hand,dealer_hand, main_code.player_chips)
    #     else:
    #         main_code.push(player_hand,dealer_hand)
    
    

def gameUI(player_hand, dealer_hand, deck):
    gp = Tk()
    gp.resizable(width= False, height= False)
    WW = 900
    WH = 400
    SW = gp.winfo_screenwidth()
    SH = gp.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    gp.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    gp.title('Blackjack')
    gp.config(bg='green')

    bt1 = Button(gp, text='Hit', font=(20), width=5, command= lambda: HIT(deck, player_hand, dealer_hand, gp))
    bt2 = Button(gp, text='Stand', font=(20), width=5, command= lambda: STAND(player_hand, dealer_hand, deck, gp))
    bt3 = Button(gp, text='Exit', font=(20), width=5, command= exit)
    bt1.pack(side=RIGHT, padx=10, pady=40)
    bt2.pack(side=RIGHT, padx=10, pady=40)
    bt3.pack(side=RIGHT, padx=10, pady=40)

    main_code.show_some(player_hand, dealer_hand, gp)

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
    
    gp.mainloop()

# gameUI(lst1, lst2)
