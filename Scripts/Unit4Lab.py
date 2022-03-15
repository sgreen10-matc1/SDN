#!/usr/bin/env python3

import requests # import requests module

def getCardDeck(): # creates getCardDeck function
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1" # create url variable
    
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload) # GET request "requests.request" and save it to response variable
    deck = response.json() # create the deck dictionary from response json
    deck_ID = deck["deck_id"] # Deck_ID variable that stores the "deck_id" of the deck of cards
    return deck_ID # returns the deck_ID variable from deck dictionary

def displayRules(): # create displayRules function that prints out the rules of the card game
    print("If you wish to challenge the computer to war... Here are some rules. Choose how many cards to pick\n"
          "up from 1-5, typing 0 ends the game. Then the computers takes a turn. Cards are then\n"
          "totaled up. Your cards and the computers cards are compared, whomever has the\n"
          "higher number of cards wins!") # printing/displaying the rules cont

def numCardInput(prompt,validationList): # user input, asking for number of cards, stores and returns "answer" variable
    answer = input(prompt)
    while answer not in validationList:
        print("The following are valid inputs" + str(validationList))
        answer = input(prompt)    
    return answer # returns answer variable

def drawCards(deck_ID, numberCards): # create drawCards function, this selects the quantity of cards
    url = "https://deckofcardsapi.com/api/deck/" + deck_ID + "/draw/?count=" + numberCards # url variable that inlcudes into the address the deck_ID and the number of cards the user selected

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload) # creates response variable from a GET requests.request
    cardsDraw = response.json() # creates a dictionary "cardsDraw from response.json"
    cardsDrawn = cardsDraw["cards"] # creates cardsDrawn list variable from cardsDraw
    return cardsDrawn # returns cardsDrawn list variable

def cardTotal(cardsDrawn): # creates cardTotal function from the cardsDrawn list variable
    amount = 0
    for card in cardsDrawn:
        if card["value"] == ("1"): # add the value 1 to the amount if its a 1
            value = 1
            amount = amount + value
        if card["value"] == ("2"): # add the value 2 to the amount if its a 2
            value = 2
            amount = amount + value
        if card["value"] == ("3"): # add the value 3 to the amount if its a 3
            value = 3
            amount = amount + value
        if card["value"] == ("4"): # add the value 4 to the amount if its a 4
            value = 4
            amount = amount + value
        if card["value"] == ("5"): # add the value 5 to the amount if its a 5
            value = 5
            amount = amount + value
        if card["value"] == ("6"): # add the value 6 to the amount if its a 6
            value = 6
            amount = amount + value
        if card["value"] == ("7"): # add the value 7 to the amount if its a 7
            value = 7
            amount = amount + value
        if card["value"] == ("8"): # add the value 8 to the amount if its a 8
            value = 8
            amount = amount + value
        if card["value"] == ("9"): # add the value 9 to the amount if its a 9
            value = 9
            amount = amount + value
        if card["value"] == ("10"): # add the value 10 to the amount if its a 10
            value = 10
            amount = amount + value
        if card["value"] == ("JACK"): # add the value 11 to the amount if its a JACK
            value = 11
            amount = amount + value
        if card["value"] == ("QUEEN"): # add the value 12 to the amount if it a QUEEN
            value = 12
            amount = amount + value
        if card["value"] == ("KING"): # add the value 13 to the amount if its a KING
            value = 13
            amount = amount + value
        if card["value"] == ("ACE"): # add the value 14 to the amount if its a ACE
            value = 14
            amount = amount + value
        total = amount # create total variable from the amount added from cards drawn
        
    return total # returns total variable, assigns a value to each card drawn
    
def printCardsDrawn(cardsDrawn, total): # creates the printCardsDrawn function, with cardsDrawn list variable and the total value for the amount of cards
    for card in cardsDrawn:
        print(card["value"] + " of " + card["suit"]) 
    print("Total card value is: ", total)

# Main

displayRules() # display the rules of the game
    
numberCards = numCardInput("Enter the number of cards: ", ["0", "1", "2", "3", "4", "5"]) # user input and validationlist "user selection" for how many cards user can select

if int(numberCards) == 0: # if the interger value of numberCards variable is 0
    print("All done")  # return message ending the game
else: # if user selects any card between 1 and 5
    
    deck_ID = getCardDeck() #
    
    # users turn
    cardsDrawnUser = drawCards(deck_ID, numberCards) # creates/runs cardsDrawnComputer from drawCards
    userTotal = cardTotal(cardsDrawnUser) # creates/runs the userTotal from cardTotal
    printCardsDrawn(cardsDrawnUser, userTotal) # creates/runs printCardsDrawn for the user with total
    
    # computers turn
    cardsDrawnComp = drawCards(deck_ID, numberCards) # creates/runs cardsDrawnComputer from drawCards
    compTotal = cardTotal(cardsDrawnComp) # creates/runs the compTotal from cardTotal
    printCardsDrawn(cardsDrawnComp, compTotal) # creates/runs printCardsDrawn for the computer with total
    
    if userTotal > compTotal: # if user total card value is higher, the user wins the game
        print("You Win User!! Lucky game!!\n") # print lucky game
    elif compTotal > userTotal: # else if the computer total card value is higher, the computer wins the game
        print("Computer Wins!!! User is a Loser!!!\n") # print loser
    else:
        print("TIE!!! Good Game Everyone!\n") # else if the total card value is the same for both computer and user then print good game