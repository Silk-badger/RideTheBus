
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

def player():
    playerName = input("What's your name, friend? ")
    if playerName == "Card Master":
        print("Wrong, that's my name. We're calling you billy.")
        playerName == "Billy"
        print("Anyways Billy, welcome to...\n \nRIDE! \nTHE! \nBUS!\n")
    else:
        print("Nice to meet you,", playerName, " Welcome to...\n \nRIDE! \nTHE! \nBUS!\n")
#realBeginning = False
#while realBeginning == False:
def beginGame():
    Starting = input("\nIf you're prepped, please type 'ready' to start, or 'help' for instructions.\n")
    if Starting == "help":
        print(rules)
        Starting = input()
    elif Starting == "ready":
        #realBeginning = True
        print("-to be written.-")
    else:
        print("That's not a correct input. Do note, it's cap sensitive.\n")
        Starting = input()

#Change some definitions to while loops for easier control.
