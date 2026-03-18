import random


rules = "\nYou will play 1-4 rounds, depending on which round you decide to cash in on, \n or which round you loose on. " \
"The rounds are described and ruled as follows, in order. \n" \
"\n 1st play - Guess the color of the beginning card drawn. Guess correctly and get *2 multiplier to the amount put in. \n" \
"\n \t 2nd play - Guess if the next card given will be higher or lower than the previous, for a *3 multiplier of your chips. \n" \
"\n \t \t 3rd play - Guess if the next card will be on the inside or outside of the previous two cards for a *4 multiplier \n" \
"\t \t (aka, if round one was a 4 and round 2 was a 6, 5 would be inside and anything else would be outside) \n" \
"\n \t \t \t 4th play (final round) - Guess the suit of the final card drawn for a *10 jackpot. \n \n" \
"\n NOTE: There is no pause between rounds, so type cash to cashout on the round you're on or keep playing.\n" \
"NOTE: there is no point where captials are needed, so please continually use lowercase.\n" \
"\nOnce you've finished reading, please type ready to start."

chips = 500

Suits_list = ["Clubs", "Hearts", "Diamonds", "Spades"]

Color_list = ["Red", "Black"]

Card_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

#Implement shuffle()
#Implement a random number generator

playerName = "" #setting the name blank will make it adjustable.
Gameplay = True
global player

if chips <= 0:
    print(f"\nlooks like you're done for, {playerName}. Better luck next time!")
    exit()

def player():
    global Gameplay
    global playerName #Learned what global was from W3 (See Python global Keyword)
    playerName = input("What's your name, friend? ")
    if playerName == "Card Master":
        print("Wrong, that's my name. We're calling you Billy.")
        playerName == "Billy"
        print("Anyways Billy, welcome to...\n \nRIDE! \nTHE! \nBUS!\n")
        Gameplay = False
    
    else:
        print("Nice to meet you,", playerName, " Welcome to...\n \nRIDE! \nTHE! \nBUS!\n")
        Gameplay = False


def beginGame():
    global Gameplay
    global chips
    global playerName
    Starting = input("\nIf you're prepped, please type 'ready' to start, or 'help' for instructions.\n")
    
    if Starting == "help":
        print(rules)
        beginGame()

    elif Starting == "ready":
        Gameplay = True
        print("\nGreat, let's get into it!\n")
        print("\nTo start, it looks like you have", chips, "Chips!\n")

        deck = shuffleDeck()

        validBet = False

        while not validBet: #Created and refurbished to make sure the number selected is applicable.
            bet = int(input(f"\nPlease place your bet, {playerName}. (numbers only!)\n"))
            if bet < 10 or bet > 100:
                print("Sorry pal, you can't bet under 10 or over 100, please try again.")
                bet = int(input(f"\nPlease place your bet, {playerName}.\n"))
            elif bet >= 10 and bet <= 100: 
                chips -= bet #-= subtracts an operator
                validBet = True

            
        result, bet, first_card = firstRound(deck, bet)
        
        if result: #Code for each round's result.
            #Everything below here is relatively simple, each line is for whether you win or loose a round. 
            print(f"\nCurrently, you have {bet} winnings, {playerName}")
            result, bet, secondCard = secondRound(deck, bet, first_card)
            if result: 
                print(f"\nAlrighty {playerName}, looks like you've got {bet} winnings.")
                result, bet, thirdCard = thirdRound(deck, bet, first_card, secondCard)
                if result:
                    print(f"\nfinal round, {playerName}. Time to gamble with {bet} chips.")
                    result, bet, fourthCard = finalRound(deck,bet)
                    if result:
                        print(f"So {playerName}... you get to walk away with walk away with {chips}.")
                    else:
                        print(f"\nYikes! You've lost... looks like you're at {chips} chips now.")
                        playAgain()
                else:
                    print(f"\nUnlucky!! You've lost... looks like you're at {chips} chips now.")
                    playAgain()
            else:
                print(f"\nAll the way to round three, dang... looks like you're at {chips} chips now.")
                playAgain()
        else:
            print(f"\nSo close!... looks like you're at {chips} chips now.")
            playAgain()
    else:
        print("That's not a correct input. Do note, it's cap sensitive.\n")
        beginGame()

if Gameplay == False:
    beginGame()

card = (Color_list, Card_list, " of ", Suits_list)

def shuffleDeck():
    deck = []
    for suit in Suits_list:
        for value in Card_list:
            deck.append((value, suit))
    random.shuffle(deck)
    return deck

def drawCard(deck):
    return deck.pop() #.pop removes the most recent element from the cards list (see w3 def).
    #this was below, but I moved it up for priority sake.

def playAgain():
    keepGoing = input(f"\nWould you like to keep playing, {playerName}? Type 'yes' for yes.\n")
    if keepGoing == "Yes" or keepGoing == "yes":
        beginGame()
    else:
        print(f"\nThank you for playing, {playerName}. It was fun!\n")
        exit()

def midRound():
    print(f"Smart choice, {playerName}. Cashing in so you have {chips} chips. ")
    playAgain()

def firstRound(deck, bet): #beginning/actual first round code.
    guess = input(f"\nFirst round {playerName}, type 1 for Red or 2 for Black..\n")
    card = drawCard(deck)
    value, suit = card #Gets the value/suit of the card (you'll see this code a lot.)
    if guess == "1":
        guess = "Red"
    elif guess == "2":
        guess = "Black"
    else:
        print("Incorrect, try again ")
        return firstRound(deck, bet)

    if suit in ["Hearts", "Diamonds"]:
        Color = "Red" #Only red cards can be Hearts or Diamonds
    else: Color = "Black" #The same goes for black cards being Spades or Clubs.

    print(f"{playerName}, here we go... you drew.. \n\n", value, " of ", suit)

    if guess == Color: 
        print("\nAhh, lucky start!\n")
        return True, bet *2, card
    else:
        print(f"\nUnlucky! looks like {playerName} is a loser today! (unless they didn't follow rules with the input...)\n")
        return False, 0, card
    

def secondRound(deck, bet, previousCard): 
    guess = input("\nAlrighty, round 2... will this next card be higher, or lower than the previous?\n")
    card = drawCard(deck)
    value, suit = card

    current_value = ValueofCard(value)
    previous_value = ValueofCard(previousCard[0])  
    print("\nYour next card is...", value, "of", suit,"\n")
    
    if guess == "cash": #this, as seen in lower pieces, lets you cash in mid round.
        global chips
        chips += bet
        midRound()
        return False, bet, None  
    elif (guess == "higher" and current_value > previous_value) or \
       (guess == "lower" and current_value < previous_value):
        print(f"\nAhh {playerName}, Lucky guess!", value, " was ", guess, " then ", previousCard[0], ".") 
        return True, bet *3, card
    else:
        print(f"\nOh darn! Looks like {playerName} was unlucky!\n")
        print(value, " wasn't ", guess, " than ", previousCard[0], ".")
        return False, 0, card
    
def thirdRound(deck, bet, card1, card2):
    guess = input("\nThird round, almost there... will the next card be inside or outside the previous? \n")
    
    value, suit = drawCard(deck)

    v1 = ValueofCard(card1[0])
    v2 = ValueofCard(card2[0])
    current = ValueofCard(value)

    low = min(v1, v2)
    high = max(v1, v2)

    previousCard = ValueofCard(value)
    print(f"{playerName} pulls... a ", value, " of ", suit)

    if guess == "cash":
        global chips
        chips += bet
        midRound()
        return False, bet, None  
    elif (guess == "inside" and low < current < high) or \
       (guess == "outside" and (current < low or current > high)):
        print(f"\nGreat luck {playerName}... are you cheating?\n")
        return True, bet * 4, (value, suit)
    else:
        print("\nThere's that lady luck, kicking you down!\n")
        return False, 0, (value, suit)
    
def finalRound(deck, bet, previousCard):
    guess = input(f"\nHere it is {playerName}, the big finale... All the big bucks... What Suit will the next card be?\n")
    card = drawCard(deck)
    value, suit = card
    print("\nThe final card... is..\n\n", value, " of ", suit, "!\n")

    if guess == suit:
        print(f"\nJACKPOT!! BIG WINNER!! {playerName} WINS THE GAME!!!\n")
        return True, bet *10, card
    elif guess == "Cash":
        global chips
        bet += chips
        midRound()
        return False, bet, None  
    else:
        print("\nLooks like the suit was ", suit, ".")
        print(f"\nOh man, {playerName}... I was actually rooting for you.. better luck next time!\n")
        return False, 0, card

def ValueofCard(card):
    values = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "King":12, "Queen":13}
    return values[card]
