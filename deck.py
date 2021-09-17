# Attributes & methods for making and using a deck of Life Twists & Turns cards.
import os
from console.utils import wait_key
import pickle

# Function to clear terminal window: clear()
clear = lambda: os.system('clear')

deckName = 'myDeck'
categories= ['Earn It!', 'Learn It!', 'Live It!', 'Love It!']


# Method for formating and displaying a card. Expects a single dictionary argument
def cardView(card):   # card is a dict containing keys and tuple items
    print('')
    for key,txt_tuple in card.items():
        print(key)
        print('\t',txt_tuple[0],'\n\t',txt_tuple[1],'\n')


# Method for getting deck from serialized deck file
def getDeck():
    try:
        with open(deckName, 'rb') as deckFile:
            allCards = pickle.load(deckFile)
        return allCards
    except FileNotFoundError:
        raise RuntimeError('No local serialized deck file found. Please initialize a new deck...')


# Method for dumping deck into a serialized deck file. Can also be used to initialize a deck
def dumpDeck(allCards):
    with open(deckName, 'wb') as deckFile:
            pickle.dump(allCards, deckFile)


# Method for searching through a subset of a deck object. Returns a card index of the given subset
def scrollDeck (allCards, validInd):    # allCards is a list containing card dict objects
                                        # validInd is a list of intergers (defines subset)
    clear()
    i = len(validInd) - 1   # Index for current card being viewed, to be returned upon selection
    print('Here is the most recent card:\n')
    while(True):
        cardView(allCards[validInd[i]])
        print('\n%s of %s\n' % ((i+1),len(validInd)))
        usr_sel = input('\nPress P to see previous card\tPress N to see next card\tPress S to select/exit\n\nTo see a specific card, enter an index number\n\nChoose an option: ').lower()
        clear()
        if (usr_sel == 'p') and (i > 0):
            print('Here is the previous card:\n')
            i -= 1
        elif (usr_sel == 'p') and (i <= 0):
            print('There is not a previous card. Here is the current card:\n')
        elif (usr_sel == 'n') and (i < (len(validInd)-1)):
            print('Here is the next card:\n')
            i += 1
        elif (usr_sel == 'n') and (i >= (len(validInd)-1)):
            print('There is not a next card. Here is the current card:\n')
        elif (usr_sel.isnumeric() and (int(usr_sel) <= len(validInd)) and (int(usr_sel) > 0)):
            print('Here is the specified card:\n')
            i = int(usr_sel) - 1
        elif (usr_sel == 's'):
            cardView(allCards[validInd[i]])
            print('\nThis card has been selected!')
            break
        else:
            print('Invalid input. Here is the current card:\n')
    return i


# I started making a Class, but determined that I was too lazy to use it.
class LifeDeck():
    
    # List of all created cards
    cards = []
    
    def __init__(self,name):
        self.name = name

    def cardView(self, drawnCard):
        print('')
        for key,txt_tuple in drawnCard.items():
            print(key)
            print('\t',txt_tuple[0],'\n\t',txt_tuple[1],'\n')
