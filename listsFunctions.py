import random


rules = "\nYou will play 1-4 rounds, depending on which round you decide to cash in on, \n or which round you loose on. " \
"The rounds are described and ruled as follows, in order. \n" \
"\n 1st play - Guess the color of the beginning card drawn. Guess correctly and get *2 multiplier to the amount put in. \n" \
"\n \t 2nd play - Guess if the next card given will be higher or lower than the previous, for a *3 multiplier of your chips. \n" \
"\n \t \t 3rd play - Guess if the next card will be on the inside or outside of the previous two cards for a *4 multiplier \n" \
"\t \t (aka, if round one was a 4 and round 2 was a 6, 5 would be inside and anything else would be outside) \n" \
"\n \t \t \t 4th play (final round) - Guess the suit of the final card drawn for a *10 jackpot. \n \n" \
"Once you've finished reading, please type ready to start.\n"

chips = 500

Suits_list = ["Clubs", "Hearts", "Diamonds", "Spades"]

Color_list = ["Red", "Black"]

Card_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

#Implement shuffle()
#Implement a random number generator

Gameplay = False

def player():
    playerName = input("What's your name, friend? ")
    if playerName == "Card Master":
        print("Wrong, that's my name. We're calling you billy.")
        playerName == "Billy"
        print("Anyways Billy, welcome to...\n \nRIDE! \nTHE! \nBUS!\n")
        Gameplay = True
    else:
        print("Nice to meet you,", playerName, " Welcome to...\n \nRIDE! \nTHE! \nBUS!\n")
        Gameplay = True

def beginGame():
    Starting = input("\nIf you're prepped, please type 'ready' to start, or 'help' for instructions.\n")
    if Starting == "help":
        print(rules)
        Gameplay = True
    elif Starting == "ready":
        print("\nGreat, let's get into it!\n")
        print("\nTo start, it looks like you have", chips, "Chips!\n")
        Gameplay = False
        firstRound()
    else:
        print("That's not a correct input. Do note, it's cap sensitive.\n")
        Gameplay = True

while Gameplay == True:
    print(beginGame)

def shuffleDeck():
    deck = []
    for suit in Suits_list:
        deck.append((card, suit))
    random.shuffle(deck)
    return

def ValueofCard(card):
    values = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "King":12, "Queen":13}
    return values[card]

#After a little research on W3Schools, I've learned of .pop, which removes an item from the list and returns it.

def drawCard(deck):
    return deck.pop()

def betweenRounds(currentBet): #created this to give the player a chance to relearn rules or cashout.
    
    while True: 
    
        nextSteps = input("\nAlrighty, you're between rounds. Need help, want to cashout, or ready to continue? (Remember, no capitals) \n ")
        if nextSteps == "help":
            print(rules)
            betweenRounds = True

        elif nextSteps == "cashout": 
            nextSteps = False
            print("\nLooks like you're cashing out at ", chips)
            print("Thank's for playing, ", player, " it was fun! hope to see you again soon.")
            exit(0)

        elif nextSteps == "continue":
            nextSteps = False
            continue

        else:
            print("\nThat's not a correct input, give it another shot. \n")
            nextSteps = True



def firstRound(deck, bet):
    guess = input("Alright, then... First: Red or Black?\n")

    card = drawCard(deck)
    value, suit = card

    Color = "Red" if suit in ["Hearts", "Diamonds"] else "Black"
    print("\nLet's see it, looks like you drew...\n\n", value, "of", suit)

    if guess == Color:
        print("\nwinner winner! lucky start!\n")
        return True, bet *2, card
        print("Now you're at ", chips)
        betweenRounds = True
    else:
        print("\nUh oh, loser alert!\n")
        return False, 0, card
        print("Now you're at ", chips, "\n")
        betweenRounds = True


#Change some definitions to while loops for easier control.
