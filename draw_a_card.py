#!/usr/bin/env python3
# Tool script for drawing cards from a serialized deck object
import os
import random
from console.utils import wait_key
import deck


# Create Python function clear() from Linux clear function to clear terminal window
clear = lambda: os.system('clear')


# Import cardlist
allCards = deck.getDeck()


# Initialize & main code
clear()
print('Welcome to Card Draw!')
drawnCards = []     # list of indeces for all drawn cards

while(True):
    print('\nReturn D to draw a card\t\tReturn R to review previously drawn cards\t\tReturn X to exit\n')
    cmd = input('\nPlease select an option: ').lower()
    clear()

    if cmd == 'd':        # draw a card
        i = random.randint(0,(len(allCards)-1))
        while(i in drawnCards):
            i = random.randint(0,(len(allCards)-1))
        print('Here is your card: ')
        deck.cardView(allCards[i])
        drawnCards.append(i) # note card's allCards index so it can't be drawn again until reshuffle
        if (len(drawnCards) == len(allCards)): # if all cards have been drawn, reshuffle
            print('All cards have been drawn, press any key to reshuffle\n')
            wait_key()
            drawnCards = []
            clear()
            print('All cards have been drawn, so the deck has been reshuffled\n')

    elif cmd == 'r': 
        if (len(drawnCards) <= 0):
            print('\nNo cards have been drawn\n')
        else:
            #j = drawnCards[len(drawnCards)-1]   # allCards index of the last card drawn
            #deck.cardView(allCards[j])          # create scrollDeck function and replace this line
            deck.scrollDeck(allCards, drawnCards)

    elif cmd == 'x':      # exit Card Draw
        print('\nExiting Card Draw...')
        break
