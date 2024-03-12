import random

# Create a deck of cards

def create_deck():
    deck = []
    for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        for rank in range(2, 11):
            deck.append(str(rank) + " of " + suit)
        for face in ['Jack', 'Queen', 'King', 'Ace']:
            deck.append(face + " of " + suit)
    return deck

# Shuffle the deck

def shuffle_deck(deck):
    for i in range(len(deck)):
        j = random.randrange(len(deck))
        deck[i], deck[j] = deck[j], deck[i]

# Deal a hand

def deal(deck):
    hand = []
    for i in range(2):
        hand.append(deck.pop(0))
    return hand

def value(hand):
    value = 0
    for card in hand:
        if card.split()[0] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card.split()[0] == 'Ace':
            value += 11
            if value > 21:
                value -= 10
        else:
            value += int(card.split()[0])
    return value

# Play the game

def player_choice():
    choice = ""
    while choice not in ["h", "s"]:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
    return choice

def play_game():
    playerWin = False
    playerLoose = False
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = deal(deck)
    dealer_hand = deal(deck)
    valuePlayer = value(player_hand)
    valuedealer = value(dealer_hand)
    print("Player's hand:", player_hand, " Value:", valuePlayer)
    print("Dealer's hand:", dealer_hand, " Value:", valuedealer)
    if valuedealer == 21 and valuePlayer == 21:
        print("Push!")
    elif valuedealer == 21:
        print("Black jack! Dealer wins!")
    elif valuePlayer == 21:
        print("Black jack! Player wins!")
    else:
        while True:
            choice = player_choice()
            if choice == "h":
                player_hand.append(deck.pop(0))
                print("Player's hand:", player_hand , " Value:", value(player_hand))
                if value(player_hand) > 21:
                    print("Player busts!")
                    playerLoose = True
                    break
                elif value(player_hand) == 21:
                    print("Player wins!")
                    playerWin = True
                    break
            else:
                break
                
        while playerWin == False and playerLoose == False:
            if value(dealer_hand) < 17 and value(dealer_hand) < value(player_hand) and value(player_hand) <= 21:
                dealer_hand.append(deck.pop(0))
                valuedealer = value(dealer_hand)
                print("Dealer's hand:", dealer_hand, " Value:", value(dealer_hand))
                if value(dealer_hand) > 21:
                    print("Dealer busts!")
                    break
                elif value(dealer_hand) == 21:
                    print("Dealer wins!")
                    break
                elif value(dealer_hand) > value(player_hand) and value(dealer_hand) < 21:
                    print("Dealer wins!")
                    break
                elif value(dealer_hand) == value(player_hand):
                    print("Push!")
                    break   
                else:
                    continue
            else:
                if value(dealer_hand) > value(player_hand) and value(dealer_hand) < 21:
                    print("Dealer wins!")
                    break
                elif value(dealer_hand) == value(player_hand):
                    print("Push!")
                    break
                else:
                    print("Player wins!")
                    break
play_game()

