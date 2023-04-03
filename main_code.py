import random

values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
        'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

suit=('Hearts','Diamonds','Clubs','Spade')

rank=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack',
      'Queen','King','Ace')

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return self.rank + " of " + self.suit

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
    
    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet:"))
        except:
            print("Sorry please provide an integer....")
        else:
            if chips.bet > chips.total:
                print('Sorry, you dont have enough chips to place the bet. You have {}'.format(chips.total))
            else:
                break
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_cards(single_card)
    hand.adjust_for_ace()

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

def show_some(player,dealer):
    #Show only one of dealer's card
    
    print("\n Dealer's hand")
    print("First card hidden")
    print(dealer.cards[1])
    
    #Show all of (2) the player's cards
    print("\n Player's hand")
    for card in player.cards:
        print(card)
        
def show_all(player,dealer):
    #Show all the dealer's cards
    
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)
        
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

while True:
    
    print("WELCOME TO BLACKJACK!!!")
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
    
    player_chips = Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
    print("\n Player total chips are at: {}".format(player_chips.total))
    
    new_game = input("Would you like to play again? Enter y or n")
    
    if new_game.lower == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing.....")
        break
