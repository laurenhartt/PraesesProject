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

    def getPPoints(self):
        points = 0
        face = ["King","Queen","Jack"]

        for value in self.playerHand:
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

    def getDPoints(self):
        points = 0
        face = ["King","Queen","Jack"]

        for value in self.dealerHand:
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

def playerHit(hand, deck, points):
    hand.playerHand.append(random.choice(deck))
    print("\033[4mYour current hand:\033[0m")

    for index in range(0, len(hand.playerHand)):
        i = hand.playerHand[index]
        print(i)

    points = hand.getPPoints()
    print("Your points:")
    print(points)
    print("--------")
    return points

def dealerStart(hand, points):
    print("\033[4mDealer's hand:\033[0m")

    for index in range(0, len(hand.dealerHand)):
        i = hand.dealerHand[index]
        print(i)

    points = hand.getDPoints()
    print("--------")
    print("dealer's points:")
    print(hand.getDPoints())
    print("--------")
    return points

def BlackJack():
    money = 100
    print("---------------------------------------")
    print("Welcome to BlackJack!")
    print("You have a starting amount of $100! Play till you lose it all! (or get bored)")
    while money >= 10:
        print("Minimum bet is $10!")

        while True:
            amountToBet = input("How much would you like to bet? (Type 0 to exit): ")
            if not amountToBet.isdigit():
                print("That input was not an integer number")
            else:
                if 10 > int(amountToBet) > 0:
                    print("Oops! The bet minimum is $10! Try again")
                elif int(amountToBet) == 0:
                    quit()
                elif int(amountToBet) > money:
                    print("You don't have enough for a bet that high")
                else:
                    print("current bet: ", amountToBet)
                    print("money left to spend: ", money)
                    break
        
        masterDeck = []
        masterDeck = deck*6


        playerHand = []
        playerHand.append(random.choice(masterDeck))

        dealerHand = []    
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
        print(pStarterHand.getPPoints())
        print("--------")
        print("\033[4mDealer's current hand:\033[0m")
        print("?")
        print(dStarterHand.dealerHand[1])

        PinPlay = True
        DinPlay = True
        count = 0
        Ppoints = 0
        Dpoints = 0
        Ppoints = pStarterHand.getPPoints()
        if Ppoints == 21:
            print("blackjack")
            money += 1.5 * int(amountToBet)
            print(f"you earned: {1.5 * int(amountToBet)} dollars")
            PinPlay = False

        while PinPlay == True:
            hitOrStay = input("Hit or stay? (H/S): ")
            if hitOrStay == "H":
                Ppoints = playerHit(pStarterHand, masterDeck, Ppoints)
                if Ppoints > 21:
                    print("you bust")
                    money -= int(amountToBet)
                    print(f"you lost: {int(amountToBet)} dollars")
                    PinPlay = False
                elif Ppoints == 21:
                    pass
                else:
                    PinPlay = True
                    count += 1

            elif hitOrStay == "S":
                Ppoints = pStarterHand.getPPoints()
                PinPlay = False
                while DinPlay == True:
                    Dpoints = dealerStart(dStarterHand, Dpoints)
                    if Dpoints  >= 17:
                        if Dpoints <= 21:
                            if Dpoints > Ppoints:
                                print("dealer wins")
                                money -= int(amountToBet)
                                print(f"you lost: {int(amountToBet)} dollars")
                                DinPlay = False
                            elif Dpoints == Ppoints:
                                print("tie")
                                print("you didn't win or lose any money")
                                DinPlay = False
                            else: 
                                print("you win")
                                money += int(amountToBet)
                                print(f"you earned: {int(amountToBet)} dollars")
                                DinPlay = False
                        else:
                            print("dealer busts, you win")
                            money += int(amountToBet)
                            print(f"you earned: {int(amountToBet)} dollars")
                            DinPlay = False
                    else:
                        dealerHand.append(random.choice(masterDeck))
                        DinPlay = True

            else:
                print("You need to type a capital H or capital S")
        print(f"Money after this round: {money}")
        print()

BlackJack()




