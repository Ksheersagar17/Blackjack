import random
from tkinter import *
from PIL import ImageTk,Image
import threading
import queue
import gamePage

values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
suit=('Hearts','Diamonds','Clubs','Spade')
rank=('2','3','4','5','6','7','8','9','10','J','Q','K','A')

playing = True


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return "assets/" + self.suit + "/" + self.rank + ".png"

class Deck:
    def __init__(self):
        self.deck=[]

        for suits in suit:
            for ranks in rank:
                created_cards=Card(suits,ranks)
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

class Hand:
    def __init__(self):
        self.cards = [] # start with an empty list like the deck class
        self.value = 0  # start with value 0
        self.aces = 0   # an attribute to keep track of the aces as it has special charecters

    def add_cards(self,card):
        # card passed in is from Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    # def adjust_for_ace(self):
    #     while self.value > 21 and self.aces:
    #         self.value -= 10
    #         self.aces -= 1

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips, b):
    chips.bet = b

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_cards(single_card)
    # hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or stand?? Enter h or s...")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("Player stands Dealer's turn..")
            playing = False

        else:
            print("Sorry I did not understand that...")
            continue
        break

def cardReloadSome(queue1):
    print("1")
    player = queue1.get()
    dealer = queue1.get()
    gp = queue1.get()

    dealerfrm = Frame(gp)
    dealerfrm.configure(background='green')
    dealerfrm.place(x=200, y=50)
    
    playerfrm = Frame(gp)
    playerfrm.configure(background='green')
    playerfrm.place(x=200, y=235)
    
    lab_lst = [0]*100
    pc=[0]*100
    r = 0
    
    pc[r] = Image.open('assets/B.png')
    pc_res_img1 = pc[r].resize((80,100))
    pc[r] = ImageTk.PhotoImage(pc_res_img1)
    lab_lst[r] = Label(dealerfrm, image=pc[r])
    lab_lst[r].grid(column=r,row=0)
    r = r+1

    for i in dealer.cards[1:]:
        print(f'-> {i}')
        pc[r] = Image.open(str(i))
        pc_res_img1 = pc[r].resize((80,100))
        pc[r] = ImageTk.PhotoImage(pc_res_img1)
        lab_lst[r] = Label(dealerfrm, image=pc[r])
        lab_lst[r].grid(column=r,row=0)
        r = r+1
        print(f"r = {r}")
    print("2")
    print(f"{len(player.cards)} is the length of player.cards")

    for i in player.cards:
        print(f"{i} inside cardReloadSome")
        print(f'-> {i}')
        pc[r] = Image.open(str(i))
        pc_res_img1 = pc[r].resize((80,100))
        pc[r] = ImageTk.PhotoImage(pc_res_img1)
        lab_lst[r] = Label(playerfrm, image=pc[r])
        lab_lst[r].grid(column=r,row=0)
        print(f"r = {r}")
        r = r+1
    print("3")
    gp.mainloop()
    
    

def cardReloadAll(gp, player, dealer):
    dealerfrm = Frame(gp)
    dealerfrm.configure(background='green')
    dealerfrm.place(x=200, y=50)

    playerfrm = Frame(gp)
    playerfrm.configure(background='green')
    playerfrm.place(x=200, y=235)

    lab_lst = [0]*5
    pc=[0]*5
    r = 0
    
    for i in dealer.cards:
        print(f'-> {i}')
        pc[r] = Image.open(str(i))
        pc_res_img1 = pc[r].resize((80,100))
        pc[r] = ImageTk.PhotoImage(pc_res_img1)
        lab_lst[r] = Label(dealerfrm, image=pc[r])
        lab_lst[r].grid(column=r,row=0)
        r = r+1

    for i in player.cards:
        print(f'-> {i}')
        pc[r] = Image.open(str(i))
        pc_res_img1 = pc[r].resize((80,100))
        pc[r] = ImageTk.PhotoImage(pc_res_img1)
        lab_lst[r] = Label(playerfrm, image=pc[r])
        lab_lst[r].grid(column=r,row=0)
        r = r+1
        
    gamePage.result(player, dealer, gp)

    gp.mainloop()


def show_some(player,dealer, gp):
    #Show only one of dealer's card
    queue1 = queue.Queue()
    queue1.put(player)
    queue1.put(dealer)
    queue1.put(gp)
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
    print("Middle of show_some part2")
    thread1 = threading.Thread(target=cardReloadSome, args = (queue1,))
    thread1.start()
    print("Middle of show_some part3")
    print("\n Dealer's hand")
    print("First card hidden")
    print(dealer.cards[1])
    print("Middle of show_some part4")
    #Show all of (2) the player's cards
    print("\n Player's hand")
    for card in player.cards:
        print(card)
    print("Exiting show_some")



def show_all(player, dealer, gp):
    #Show all the dealer's cards
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
    
    cardReloadAll(gp, player, dealer)

    # Calculate and display the value
    print(f"Value of Dealer's hand is : {dealer.value}")

    #Show all of player's cards
    print("\n Player's hand:")
    for card in player.cards:
        print(card)

    print(f"Value of player's hand is : {player.value}")
    
    
def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("DEALER BUSTS!PLAYER WINS!!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!BUST PLAYER!!")
    chips.lose_bet()

def push(player,dealer):
    print("Player and Dealer tie... PUSH!!")

