from tkinter import *
from PIL import ImageTk,Image
import gamePage
import main_code
import random

values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

suit=('Hearts','Diamonds','Clubs','Spade')

rank=('2','3','4','5','6','7','8','9','10','J','Q','K','A')


class Deck:
    def __init__(self):
        self.deck=[]
        
        for suits in suit:
            for ranks in rank:
                created_cards=main_code.Card(suits,ranks)
                self.deck.append(created_cards)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp = deck_comp + '\n' + card.__str__()
        return "The deck has:"+deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

def backCode(root, msg, b):
    msg.destroy()
    root.destroy()
    deck = Deck()
    deck.shuffle()
    
    player_hand = main_code.Hand()  #The player's hand storage
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
    
    dealer_hand = main_code.Hand()  #The dealer's hand storage
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
    
    player_chips = main_code.Chips()
    
    main_code.take_bet(player_chips, b)
    
    gamePage.gameUI(player_hand, dealer_hand, deck)

def cont(msg, root, b):
    backCode(root, msg, b)
    

def goin(root):
    msg = Tk()
    msg.resizable(width= False, height= False)
    WW = 470
    WH = 150
    SW = msg.winfo_screenwidth()
    SH = msg.winfo_screenheight()
    x = SW/2 - WW/2
    y = SH/2 - WH/2
    msg.geometry('%dx%d+%d+%d' %(WW, WH, x, y))
    l = Label(msg, text='Enter your Bet : ', font=(20))
    l.place(x=40, y= 40)
    ent = Entry(msg, font=(20))
    ent.place(x=200, y= 40)
    filling = Button(msg, text='Continue', font=(20), command= lambda : cont(msg, root, int(ent.get())))
    filling.pack(side=BOTTOM, padx=10, pady=20)
    msg.mainloop()



def goout(root):
    root.destroy()
    
def start():
    gameon()

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
