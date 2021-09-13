#!/usr/bin/env python3
# Tool for the creation and viewing of Life Twists & Turns cards
import os
import pickle
from console.utils import wait_key      # Waits for user to press a key
import deck


# Create function to clear terminal window: clear()
clear = lambda: os.system('clear')


# Initialize deck - only done once
def initDeck():
    if (os.path.exists(deck.deckName)):
        print('Deck already exists and will not be overwritten.\nPress any key to continue...')
    else:
        allCards = []
        deck.dumpDeck(allCards)
        print('Deck created successfully!\nPress any key to continue...')
    wait_key()


# Function to add cards and save them using pickle module
def addCard(newCard):
    try:
        allCards = deck.getDeck()
        allCards.append(newCard)
        deck.dumpDeck(allCards)
        print('Card saved successfully!')
    except FileNotFoundError:
        print('New card was not saved succesfully')

# Function to remove a selected card using pickle module
def remCard(card2rem):
    try:
        allCards = deck.getDeck()
        allCards.pop(card2rem)
        deck.dumpDeck(allCards)
        print('Card removed successfully!')
    except FileNotFoundError:
        print('Specified card index not available')


# Function to write cards
def writeCard():
    print('Welcome to card creation!')
    while(True):
        makeCard = input('\nMake a new card (y/n)? ').lower()
        
        if (makeCard == 'n'):
            print('\nReturning to main menu\nPress any key to continue...')
            wait_key()
            break
        
        elif (makeCard == 'y'):
            newCard = {}
            for i in deck.categories:
                flavorText = input('\nEnter flavor text for "%s":\n' % i)
                effectText = input('\nEnter effect for "%s":\n' % i)
                newCard[i] = (flavorText, effectText)
            clear()
            print('Your finished card will appear like this:\n')
            deck.cardView(newCard)
            while(True):
                saveConfirm = input('\nSave this card (y/n)? ').lower()
                if (saveConfirm == 'y'):
                    addCard(newCard)
                    break
                elif (saveConfirm == 'n'):
                    print('\nNew card discarded')
                    break
                else:
                    print('\nInvalid input')
        else:
            print('\nInvalid input')


# Function to view cards
def viewCard():
    allCards = deck.getDeck()
    numAll = list(range(0,len(allCards)))
    deck.scrollDeck(allCards,numAll)


# Function to delete cards
def deleteCard():
    allCards = deck.getDeck()
    numAll = list(range(0,len(allCards)))
    print('Select the card to delete\nPress any key to continue...')
    wait_key()
    card2del = deck.scrollDeck(allCards,numAll)
    while(True):
        usr_confirm = input('Are you sure you want to delete this card(y/n)? ').lower()
        if (usr_confirm == 'y'):
            remCard(card2del)
            print('Card successfully deleted!\nReturning to main menu\nPress any key to continue...')
            wait_key()
            break
        elif (usr_confirm == 'n'):
            print('Card deletion cancelled\nReturning to main menu\nPress any key to continue...')
            wait_key()
            break
        else:
            print('Invalid input')


# Function to edit cards
def editCard():
    allCards = deck.getDeck()
    numAll = list(range(0,len(allCards)))
    card2edit = deck.scrollDeck(allCards,numAll)
    print('Function under construction. Come back later...')
    wait_key()


# Main menu
funcDict = {'1': writeCard,     '2': viewCard,
            '3': deleteCard,    '4': editCard,
            '5': initDeck,      '0':'Exit'
}

while(True):
    clear()
    print('\n\n--- MAIN MENU ---')
    for key, value in funcDict.items():
        print(key, value)
    try:
        user_sel = input('\nWhat would you like to do? ')
        if user_sel == '0':
            print('Exiting...')
            break
        else:
            clear()
            funcDict[user_sel]()

    except KeyError:
        print('Key error. Desired function does not exist. Try again. Press any key to continue...')
        wait_key()
