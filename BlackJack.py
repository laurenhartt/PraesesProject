import random

suits = ("Spades","Hearts","Clubs","Diamonds")
cards = (2,3,4,5,6,7,8,9,10,"King","Queen","Jack","Ace")


playerHand = []
dealerHand = []

winnings = 0

class Card():
    def __init__(self,suits,cards):
        self.suit = suits
        self.card = cards
    def Suit(self):
        return self.suit
    def Card(self):
        return self.card
    def __str__(self):
        return str(self.card) + " of " + str(self.suit)
deck = []
for suit in suits:
    for card in cards:
        deck.append(Card(suit,card))

class Player():
    def __init__(self,playerHand):
        self.playerHand = playerHand
        
    def getHand(self):
        return self.playerHand
def getPPoints(playerHand):
    points = 0
    face = ["King","Queen","Jack"]
    for value in playerHand:
        if value.card in face:
            points += 10
        elif value.card == "Ace":
            if points >= 11:
                points += 1
            else:
                points += 11
        else:
            points += value.card
    return points

class Dealer():
    def __init__(self,dealerHand):
        self.dealerHand = dealerHand
    def getHand(self):
        return self.dealerHand
def getDPoints(dealerHand):
    points = 0
    face = ["King","Queen","Jack"]
    for value in dealerHand:
        if value.card in face:
            points += 10
        elif value.card == "Ace":
            if points >= 11:
                points += 1
            else:
                points += 11
        else:
            points += value.card
    return points


def BlackJack():
    bet = 0
    money = 20
    print("---------------------------------------")
    print("Welcome to BlackJack!")
    print("Minimum bet is $10!")
    while money >= 10:
        while True:
            amountToBet = int(input("How much would you like to bet?: "))
            if amountToBet < 10:
                print("Oops! The bet minimum is $10! Try again")
            else:
                bet += amountToBet
                break
        masterDeck = []
        masterDeck = deck*6
        playerHand = []
        dealerHand = []    
        playerHand.append(random.choice(masterDeck))
        playerHand.append(random.choice(masterDeck))
        pStarterHand = Player(playerHand)
        dealerHand.append(random.choice(masterDeck))
        dealerHand.append(random.choice(masterDeck))
        dStarterHand = Dealer(dealerHand)
        print("---------------------------------------")
        print("\033[4mYour current hand:\033[0m")
        print(pStarterHand.playerHand[0])
        print(pStarterHand.playerHand[1])
        print("--------")
        print("your points:")
        print(getPPoints(pStarterHand.playerHand))
        print("--------")
        print("\033[4mDealer's current hand:\033[0m")
        print("?")
        print(dStarterHand.dealerHand[1])
        PinPlay = True
        DinPlay = True
        count = 0
        Ppoints = 0
        Dpoints = 0
        Ppoints = getPPoints(pStarterHand.playerHand)
        if Ppoints == 21:
            print("blackjack")
            PinPlay = False
        while PinPlay == True:
            hitOrStay = input("Hit or stay? (H/S): ")
            if hitOrStay == "H":
                pStarterHand.playerHand.append(random.choice(masterDeck))
                print("\033[4mYour current hand:\033[0m")
                for index in range(0,len(playerHand)):
                    i = playerHand[index]
                    print(i)
                Ppoints = getPPoints(pStarterHand.playerHand)
                print("--------")
                print("Your points:")
                print(getPPoints(pStarterHand.playerHand))
                print("--------")
                if Ppoints > 21:
                    print("you bust")
                    PinPlay = False
                elif Ppoints == 21:
                    pass
                else:
                    PinPlay = True
                    count += 1   
            else:
                Ppoints = getPPoints(pStarterHand.playerHand)
                PinPlay = False
                while DinPlay == True:
                    print("\033[4mDealer's hand:\033[0m")
                    for index in range(0,len(dealerHand)):
                        i = dealerHand[index]
                        print(i)
                    Dpoints = getDPoints(dStarterHand.dealerHand)
                    print("--------")
                    print("dealer's points:")
                    print(getDPoints(dStarterHand.dealerHand))
                    print("--------")
                    if Dpoints  >= 17:
                        if Dpoints <= 21:
                            if Dpoints > Ppoints:
                                print("dealer wins")
                                DinPlay = False
                            elif Dpoints == Ppoints:
                                print("tie")
                                DinPlay = False
                            else: 
                                print("you win")
                                DinPlay = False
                        else :
                            print("dealer busts, you win")
                            DinPlay = False
                    else:
                        dealerHand.append(random.choice(masterDeck))
                        DinPlay = True

BlackJack()



