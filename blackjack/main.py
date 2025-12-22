import random

import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


computer_cards = []
cc1= random.choice(cards)
cc2= random.choice(cards)
computer_cards_addition = cc1+ cc2
computer_cards.append(cc1)
computer_cards.append(cc2)

player_cards = []
pc1= random.choice(cards)
pc2= random.choice(cards)
player_cards_addition = pc1 + pc2
player_cards.append(pc1)
player_cards.append(pc2)
status_continue = True
current_stuation = True

def check_cards(player_cards, computer_cards):
    if player_cards_addition <= 16:
        print("\nComputer win")
        status_continue = False
        current_stuation = False
    elif player_cards_addition > 21:
        print("\nComputer win")
        status_continue = False
        current_stuation = False

print("computer cards: ",computer_cards[1])
print("player cards: ",player_cards)
while status_continue :


    check_cards(player_cards, computer_cards)
    print("computer cards: ", computer_cards)
    print("player cards: ", player_cards)



    while current_stuation:
        next_movement = input("\n Hand or card h/c ").lower()
        if next_movement== "h":
            print("computer cards: ", computer_cards)
            print("player cards: ", player_cards)
            if player_cards_addition < computer_cards_addition:
                print("\nComputer win")
            else:
                print("\nPlayer win")
        elif next_movement == "c":
            pc = random.choice(cards)
            player_cards.append(pc)
            print("computer cards: ", computer_cards)
            print("player cards: ", player_cards)
            player_cards_addition += pc
            check_cards(player_cards, computer_cards)



