import random
import tkinter as tk

# window = Tk()

# # Load the images using PhotoImage
# card_images = [PhotoImage(file=f'card_{i}_{j}.png') for i in range(4) for j in range(13)]

# # Shuffle the deck
# random.shuffle(card_images)
# label = Label(window)
# i = 0
# for h,image in enumerate(card_images):
#     label = Label(window, image=image)
#     label.grid(row=j, column=i)
#     i += 1
#     if i == 13:
#         j += 1
#         i = 0


# # Start the Tkinter event loop
# window.mainloop()

blackJack = tk.Tk()
blackJack.title("Black Jack")
blackJack.geometry("800x500")
blackJack.configure(bg="green")

TitleLabel = tk.Label(blackJack, text="Black Jack", font=("Arial", 24), bg="green", fg="black", relief="raised", borderwidth=3)
TitleLabel.grid(row=0, column=0, columnspan=5, pady=10 ,padx=10 ,sticky="nsew")

def replay_game():
    #destroy all the widget
    for widget in blackJack.winfo_children():
        if widget != TitleLabel:
            widget.destroy()
    #start new game
    start_game()
    
    
def quit_game():
    blackJack.destroy()

def start_game():
    global i 
    i = 0
    play_game()
    startButton.destroy()
    replayButton = tk.Button(blackJack, text="Replay", font=("Arial", 16), bg="white", command=replay_game)
    quitButton = tk.Button(blackJack, text="Quit", font=("Arial", 16), bg="white", command=quit_game)
    replayButton.grid(row=2, column=0)
    quitButton.grid(row=2, column=1)
    
    

    
    
startButton = tk.Button(blackJack, text="Start", font=("Arial", 16), bg="white", command=start_game)
startButton.grid(row=1, column=0)

def create_deck():
    suits = ["0", "1", "2", "3"] #["hearts", "diamonds", "clubs", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"] #["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f"img/card_{suit}_{rank}.png")
    shuffle_deck(deck)
    return deck

def value(hand):
    value = 0
    aces = 0
    for card in hand:
        card_value = card.split("_")[2].split(".")[0]
        if card_value in ["11", "12", "13"]:
            value += 10
        elif card_value == "14":
            value += 11
            aces += 1
        else:
            value += int(card_value)
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def shuffle_deck(deck):
    random.shuffle(deck)
    
def deal(deck):
    hand = []
    for i in range(2):
        hand.append(deck.pop(0))
    return hand

i = 0

def play_game():
    global i
    deck = create_deck()
    player_hand = deal(deck)
    dealer_hand = deal(deck)
    player_label = tk.Label(blackJack, text=f"Player's hand value: {value(player_hand)}", font=("Arial", 16), bg="green", fg="white")
    dealer_label = tk.Label(blackJack, text=f"Dealer's hand value: {value(dealer_hand)}", font=("Arial", 16), bg="green", fg="white")
    player_label.grid(row=6, column=0, columnspan=5)
    dealer_label.grid(row=4, column=0, columnspan=5)
    j = 0
    for card in player_hand:
        player_cardImage = tk.Label(blackJack)
        player_cardImage.image = tk.PhotoImage(file=card)
        player_cardImage['image'] = player_cardImage.image
        player_cardImage.grid(row=5, column=i)
        i += 1
    for card in dealer_hand:
        dealer_cardImage = tk.Label(blackJack)
        dealer_cardImage.image = tk.PhotoImage(file=card)
        dealer_cardImage['image'] = dealer_cardImage.image
        dealer_cardImage.grid(row=3, column=j)
        j += 1
    hit_button = tk.Button(blackJack, text="Hit", font=("Arial", 16), bg="white")
    stand_button = tk.Button(blackJack, text="Stand", font=("Arial", 16), bg="white")
    hit_button.grid(row=8, column=0)
    stand_button.grid(row=8, column=1)
    result_label = tk.Label(blackJack, text="", font=("Arial", 16), bg="green", fg="red")
    result_label.grid(row=7, column=0, columnspan=5)
    if value(dealer_hand) == 21 and value(player_hand) == 21:
        result_label.config(text="Push!")
        hit_button["state"] = "disabled"
        stand_button["state"] = "disabled"
    elif value(dealer_hand) == 21:
        result_label.config(text="Black jack! Dealer wins!")
        hit_button["state"] = "disabled"
        stand_button["state"] = "disabled"
    elif value(player_hand) == 21:
        result_label.config(text="Black jack! Player wins!")
        hit_button["state"] = "disabled"
        stand_button["state"] = "disabled"
    
    def hit(hand, deck):
        global i
        hand.append(deck.pop(0))
        player_label.config(text=f"Player's hand value: {value(player_hand)}")
        player_cardImage = tk.Label(blackJack)
        player_cardImage.image = tk.PhotoImage(file=hand[i])
        player_cardImage['image'] = player_cardImage.image
        player_cardImage.grid(row=5, column=i)
        if value(player_hand) > 21:
            result_label.config(text="Player busts! Dealer wins!")
            hit_button["state"] = "disabled"
            stand_button["state"] = "disabled"
        elif value(player_hand) == 21:
            result_label.config(text="Player wins!")
            hit_button["state"] = "disabled"
            stand_button["state"] = "disabled"
        i += 1
            
    def stand(j, hand, deck):
        while value(dealer_hand) < value(player_hand) and value(player_hand) < 21:
            hand.append(deck.pop(0))
            dealer_label.config(text=f"Dealer's hand value: {value(dealer_hand)}")
            dealer_cardImage = tk.Label(blackJack)
            dealer_cardImage.image = tk.PhotoImage(file=hand[j])
            dealer_cardImage['image'] = dealer_cardImage.image
            dealer_cardImage.grid(row=3, column=j)
            j += 1
        if value(dealer_hand) > 21:
            result_label.config(text="Dealer busts! Player wins!")
        elif value(dealer_hand) > value(player_hand) and value(dealer_hand) < 21:
            result_label.config(text="Dealer wins!")
        elif value(dealer_hand) == value(player_hand):
            result_label.config(text="Push!")
        elif value(dealer_hand) == 21:
            result_label.config(text="Dealer wins!")
        else:
            result_label.config(text="Player wins!")
        hit_button["state"] = "disabled"
        stand_button["state"] = "disabled"
    

    hit_button.config(command=lambda: hit(player_hand, deck))
    stand_button.config(command=lambda: stand(j, dealer_hand, deck))





# Run the GUI event loop

blackJack.mainloop()