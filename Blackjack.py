
#Author: Brandon Fook Chong 

import random
import time

deck = list('23456789TJQKA'*4)
random.shuffle(deck)
value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
          '9':9, 'T':10, 'J':10, 'Q':10, 'K':10, 'A':1}

def card_count(cards):
    count = 0
    for card in cards:
        if card == "A":
            if count <= 10:
                count += 11
            else:
                count += 1
        else:
            count += value[card]
    return count

def hands(MyDeck):
    player = []
    dealer = []
    dealer.append(deck.pop())
    dealer.append(deck.pop())
    player.append(deck.pop())
    player.append(deck.pop())
    while(card_count(dealer) <= 16):
        dealer.append(deck.pop())
    return [player, dealer]

playgame = ''
MyDeck = deck
gamehands = hands(MyDeck)
HandDealer = gamehands[1]
HandPlayer = gamehands[0]

while playgame != 'exit':
    CountDealer = card_count(HandDealer)
    CountPlayer = card_count(HandPlayer)
    print ("The hand of the dealer is: ", HandDealer[0])
    print ("You have:", HandPlayer)
   
    if (CountPlayer == 21):
        print("Blackjack for the player!")
        break
    if (CountDealer == 21):
        print("Blackjack for the house!")
        break
    elif (CountPlayer > 21):
        print("Bust for the player: " + str(CountPlayer) + " is bigger than 21. The house wins!")
        break
    playgame = input("Hit or Stand?")
    if (playgame == "Hit"):
        HandPlayer.append(deck.pop())
    if (playgame == "Stand"):
        for card in HandDealer:
            print("The house hits and gets", card)
            time.sleep(0.5)
        print("The player has a total count of", str(CountPlayer))
        print("The dealer has a total count of", str(CountDealer))
        if (CountPlayer > CountDealer):
            print("The player wins!")
            break
        if (CountDealer > 21):
            print("The house Busts! The player wins!")
            break
        elif (CountPlayer == CountDealer):
            print("Tie!")
            break
        else:
            print("The house wins!")
        break 
