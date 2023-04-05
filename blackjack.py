from tkinter import *

root = Tk()
root.title("BlackJack Card Deck")
root.iconbitmap(r'C:\Users\User\OneDrive\Documents\Pgms\New folder\bj.jpg')
root.geometry("900x500+0+0")
root.configure(background = "green")

def shuffle():
   
    #define deck
   values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

   suit=('Hearts','Diamonds','Clubs','Spade')
   rank=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

#Create frames for cards
dealer_frame = LabelFrame(my_frame, text = "Dealer", bd = 0)
dealer_frame.grid(row = 0, column = 0,padx = 20, ipadx = 20)

player_frame = LabelFrame(my_frame, text = "Player", bd = 0)
player_frame.grid(row = 0, column = 1, ipadx = 20)

#Put cards in frames
dealer_label = Label(dealer_frame, text = '')
dealer_label.pack(pady = 20)

player_label = Label(player_frame, text = '')
player_label.pack(pady = 20)

#Create some buttons
shuffle_button = Button(root, text = 'Shuffle Deck', font = ("Helvetica",14), command = shuffle)
shuffle_button.pack(pady = 20)

card_button = Button(root, text = 'Get Cards', font = ("Helvetica",14))
card_button.pack(pady = 20)

root.mainloop()