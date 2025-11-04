import random #kun 2 ark med kode til eksamen 

full_deck = {"Two of clubs": 2, #dictionary av kortstokket
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

def get_random_card(): #tilfeldig velge kort-navn
    random_card= list(full_deck.keys())
    chosen_card=random.choice(random_card)
    return f'{chosen_card}'

def get_card_value(card): #vet ikke hvordan denne fungerer
    return full_deck[card]

def calculate_hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += get_card_value(card)
        if card == 11 and hand_value<=10:
            hand_value += get_card_value(card)
        elif card == 11 and hand_value>10:
            card = 1
            hand_value += get_card_value(card)
    return hand_value

def compare(dealer_hand_in, player_hand_in): #sammenlikne kort-verdiene
    if calculate_hand_value(dealer_hand_in)>21: 
        total_chips += use_chips
        print("the dealer had over 21. you won.")
    elif calculate_hand_value(player_hand_in)>calculate_hand_value(dealer_hand_in):
        total_chips += use_chips
        print("you had more than the dealer. you won.")
    elif calculate_hand_value(dealer_hand_in)>calculate_hand_value(player_hand_in):
        total_chips -= use_chips
        print("the dealer had more than you. you lost.")
    elif calculate_hand_value(dealer_hand_in)==calculate_hand_value(player_hand_in):
        print("both had same cardvalue. it is a tie.")
    elif calculate_hand_value(player_hand_in) == 21:
        total_chips += use_chips*2
        print(f'you got Blackjack! you won {use_chips*2}')

#starten av spillet
try:
    total_chips = int(input(f"how many chips do you want to have?"))
    use_chips = int(input(f"how many chips do you want to bet?"))
except ValueError:
    print("that is not a number. try again\n")
player_hand=[]
dealer_hand=[]
for hand in range(2):
    player_hand.append(get_random_card())
    dealer_hand.append(get_random_card())
print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[-1]}, with a total value of {calculate_hand_value(player_hand)}. The dealers visible card is a {dealer_hand[0]}, and a total value of {calculate_hand_value(dealer_hand)}.")

while True:
    try: #sjekke om spilleren velger riktig valg
        action=int(input("Do you wish to hit, stand or quit?\n1 - Hit\n2 - Stand\n3 - Quit\n"))
        if action >=4:
            print(f'is not a choice. try again\n')
    except ValueError:
        print("not a number. try again\n")

    if action == 1: #gi ut kortene til spilleren og dealeren
        for hand in range(1):
            player_hand.append(get_random_card())
            dealer_hand.append(get_random_card())

        if calculate_hand_value(player_hand)>21:
            print(f'you got {player_hand[-1]}.\n')
            print(f'you have:\n')
            for cards in range(len(player_hand)): #vise kortene i en fin rekkefølge
                print(f'{player_hand[cards]}')
            print(f"you had a total of {calculate_hand_value(player_hand)}. you lost.")
            player_hand.clear()
            dealer_hand.clear()
            choice=input("\nplay again? (y/n)")
            choice.lower()
            if choice=="y": #spille igjen
                for hand in range(2):
                    player_hand.append(get_random_card())
                    dealer_hand.append(get_random_card())
                print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[-1]}, with a total value of {calculate_hand_value(player_hand)}. The dealers visible card is a {dealer_hand[0]}, with a value of {calculate_hand_value(dealer_hand)}.")
                continue
            elif choice=="n": #avslutte
                break

        elif calculate_hand_value(player_hand)<21: #fortsette runden
            print(f'you have {player_hand} and a total value of {calculate_hand_value(player_hand)}')
            continue

        elif calculate_hand_value(player_hand)==21:
            total_chips += use_chips*2
            print(f'you got Blackjack! you won {use_chips*2}')

    elif action == 2:
        while True: #gi kort til dealeren til mer eller mindre enn 17
            if calculate_hand_value(dealer_hand) <= 17:
                dealer_hand.append(get_random_card()) 
            elif calculate_hand_value(dealer_hand) > 17:
                break
        print(f'\nThe dealers cards are:') #vise kortene på en fin rekkefølge
        for x in dealer_hand:
            print(x) 
        print(f'with a value of {calculate_hand_value(dealer_hand)}\n\nyour cards are:')
        for x in player_hand:
            print(x)
        print(f'with a value of {calculate_hand_value(player_hand)}\n')
        
        compare(dealer_hand,player_hand) #sammenlikne kort-verdiene
        player_hand.clear()
        dealer_hand.clear()
        choice=input("\nplay again? (y/n)")
        choice.lower()
        if choice=="y": #spille igjen
            for hand in range(2):
                player_hand.append(get_random_card())
                dealer_hand.append(get_random_card())
            print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[-1]}, with a total value of {calculate_hand_value(player_hand)}. The dealers visible card is a {dealer_hand[0]}, with a value of {calculate_hand_value(dealer_hand)}.")
            continue
        elif choice=="n": #avslutte
            break

    elif action == 3: #avslutte
        break