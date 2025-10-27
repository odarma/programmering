import random
full_deck = {"Two of clubs": 2, 
            "Three of clubs": 3, 
            "Four of clubs": 4, 
            "Five of clubs": 5, 
            "Six of clubs": 6,
            "Seven of clubs": 7, 
            "Eight of clubs": 8, 
            "Nine of clubs": 9, 
            "Ten of clubs": 10,
            "Jack of clubs": 10, 
            "Queen of clubs": 10, 
            "King of clubs": 10, 
            "Ace of clubs": 11,
            "Two of diamonds": 2, 
            "Three of diamonds": 3, 
            "Four of diamonds": 4,
            "Five of diamonds": 5,
            "Six of diamonds": 6, 
            "Seven of diamonds": 7, 
            "Eight of diamonds": 8,
            "Nine of diamonds": 9,
            "Ten of diamonds": 10, 
            "Jack of diamonds": 10,
            "Queen of diamonds":10, 
            "King of diamonds": 10,
            "Ace of diamonds": 11,
            "Two of hearts": 2, 
            "Three of hearts": 3, 
            "Four of hearts": 4, 
            "Five of hearts": 5, 
            "Six of hearts": 6,
            "Seven of hearts": 7, 
            "Eight of hearts": 8, 
            "Nine of hearts": 9, 
            "Ten of hearts": 10,
            "Jack of hearts": 10, 
            "Queen of hearts": 10, 
            "King of hearts": 10,
            "Ace of hearts": 11,
            "Two of spades": 2, 
            "Three of spades": 3,
            "Four of spades": 4, 
            "Five of spades": 5, 
            "Six of spades": 6,
            "Seven of spades": 7, 
            "Eight of spades": 8, 
            "Nine of spades": 9, 
            "Ten of spades": 10,
            "Jack of spades": 10, 
            "Queen of spades": 10, 
            "King of spades": 10,
            "Ace of spades": 11}

def get_random_card():
    random_card= list(full_deck.keys())
    chosen_card=random.choice(random_card)
    return f'{chosen_card}'

def get_card_value(card):
    return full_deck[card]

def calculate_hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += get_card_value(card)
    return hand_value

def bet():
    try:
        int(input("how many chips do you bet?"))
    except ValueError:
        print("that is not a number. try again\n")
    return

def compare(player_value_in, dealer_value_in):
    dealer_value = calculate_hand_value(dealer_value_in)
    player_value= calculate_hand_value(player_value_in) 
    if dealer_value>21:
        print("the dealer had over 21. you won.")
        
    elif player_value>dealer_value:
        print("you had more than the dealer. you won.")
    elif dealer_value>player_value:
        print("the dealer had more than you. you lost.")
    elif dealer_value==player_value:
        print("both had same cardvalue. it is a tie.")

player_hand=[]
dealer_hand=[]
for hand in range(2):
    player_hand.append(get_random_card())
    dealer_hand.append(get_random_card())
print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[-1]}, with a total value of {calculate_hand_value(player_hand)}. The dealers visible card is a {dealer_hand[0]}, with a value of {calculate_hand_value(dealer_hand)}.")

while True:
    try:
        action=int(input("Do you wish to hit, stand or quit?\n1 - Hit\n2 - Stand\n3 - Quit\n"))
    except ValueError:
        print("invalid. try again\n")

    if action == 1:
        for hand in range(1):
            player_hand.append(get_random_card())
            dealer_hand.append(get_random_card())

        if calculate_hand_value(player_hand)>21:
            print(f'you got {player_hand[-1]}.\n')
            print(f'you have:\n')
            for cards in range(len(player_hand)):
                print(f'{player_hand[cards]}')
            print(f"you had a total of {calculate_hand_value(player_hand)}. you lost.")
            player_hand.clear()
            dealer_hand.clear()
            choice=input("\nplay again? (y/n)")
            choice.lower()
            if choice=="y":
                for hand in range(2):
                    player_hand.append(get_random_card())
                    dealer_hand.append(get_random_card())
                print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[-1]}, with a total value of {calculate_hand_value(player_hand)}. The dealers visible card is a {dealer_hand[0]}, with a value of {calculate_hand_value(dealer_hand)}.")
                continue
            elif choice=="n":
                break

        elif calculate_hand_value(player_hand)<21:
            print(f'you have {player_hand} and a total value of {calculate_hand_value(player_hand)}')
            continue

    elif action == 2:
        print(f'The dealers cards are:\n{dealer_hand}\nwith a value of {calculate_hand_value(dealer_hand)}\nyour cards are:\n{player_hand}\nwith a value of {calculate_hand_value(player_hand)}')
        compare(player_hand,dealer_hand)

    elif action == 3:
        break