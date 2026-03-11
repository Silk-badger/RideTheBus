import random


rules = "\nYou will play 1-4 rounds, depending on which round you decide to cash in on, \n or which round you loose on. " \
"The rounds are described and ruled as follows, in order. \n" \
"\n 1st play - Guess the color of the beginning card drawn. Guess correctly and get *2 multiplier to the amount put in. \n" \
"\n \t 2nd play - Guess if the next card given will be higher or lower than the previous, for a *3 multiplier of your chips. \n" \
"\n \t \t 3rd play - Guess if the next card will be on the inside or outside of the previous two cards for a *4 multiplier \n" \
"\t \t (aka, if round one was a 4 and round 2 was a 6, 5 would be inside and anything else would be outside) \n" \
"\n \t \t \t 4th play (final round) - Guess the suit of the final card drawn for a *10 jackpot. \n \n" \
"\n NOTE: There is no pause between rounds, so cashout on the round you're on or keep playing.\n" \
"\nOnce you've finished reading, please type ready to start.\n"

chips = 500

Suits_list = ["Clubs", "Hearts", "Diamonds", "Spades"]

Color_list = ["Red", "Black"]

Card_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

#Implement shuffle()
#Implement a random number generator

Gameplay = True

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
    Starting = input("\nIf you're prepped, please type 'ready' to start, or 'help' for instructions.\n")
    
    if Starting == "help":
        print(rules)

    elif Starting == "ready":
        Gameplay = True
        print("\nGreat, let's get into it!\n")
        print("\nTo start, it looks like you have", chips, "Chips!\n")

        deck = shuffleDeck()

        bet = int(input("Please place your bet, ", player))
        if bet < 10 or bet > 100:
            print("Sorry pal, you can't bet under 10 or over 100, please try again.")
        elif bet > 10 and bet < 100: 
            chips.append(bet)
        
        result, bet, first_card = firstRound(deck, bet)


    else:
        print("That's not a correct input. Do note, it's cap sensitive.\n")

card = (Color_list, Card_list, "of", Suits_list)

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


def firstRound(deck, bet): #Code for first round. 
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
