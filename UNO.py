
# Made by Jongmin & Elsa

# List of improvements added to the code:
    # Implemented a +2 card (The next player draws 2 cards and lose their turn)
    # Implemented a feature that skips the player's turn if the player chooses an invalid card
    # Implemented a feature that it ends the game when the deck runs out of cards
    # Implemented a feature that announces the winner of the game

import random

colours = ('red', 'Yellow', 'Blue', 'Green')

ranks = list(range(1, 11))
ranks.append("+2")

deck = [(rank, colour) for rank in ranks for colour in colours]

random.shuffle(deck)

def deal_cards(n):
    hand = []
    for i in range(n):
        hand.append(deck.pop(0))
    return hand

def start_game(deck):
    p1 = deck[:7]
    p2 = deck[7:14]
    deck = deck[14:]

    face_up = deck.pop(0)
    main_loop(p1, p2, face_up, deck)

def main_loop(p1, p2, face_up, deck):
    current = 0
    while len(p1) > 0 and len(p2) > 0:

        print("----------------------")
        print(f"It is player {current + 1}'s turn")
        print(f"The face up card is {face_up}")
        print(f"Player {current + 1}'s hand is {p1}")

        ans = int(input("Would you like to play (enter 1) or draw (enter 2): "))
        if ans == 1:
            if len(deck) != 0:
                index = int(input("What is the index of the card you want to play?: ")) - 1
                is_vaild = vaild_play(face_up, p1[index])
                if is_vaild:
                    p1_rank = p1[index][0]
                    if p1_rank == "+2":
                        face_up = p1.pop(index)
                        add_card_1 = deck.pop(0)
                        add_card_2 = deck.pop(0)
                        p2.append(add_card_1)
                        p2.append(add_card_2) 
                        # When a '+2' is played the next player must draw 2 cards and lose their turn (Official UNO rule)
                    else:
                        face_up = p1.pop(index)
                        p1, p2 = p2, p1
                        current = (current + 1) % 2
                else:
                    print("----------------------")
                    print("Your play is invalid")
                    print("You lost your turn") 
                    p1, p2 = p2, p1
                    current = (current + 1) % 2
            else:
                print("GAME OVER")
                print("The deck is out of cards to draw from")
                return
        elif ans == 2:
            if len(deck) != 0:
                p1.append(deck.pop(0))
                p1, p2 = p2, p1
                current = (current + 1) % 2
            else:
                print("GAME OVER")
                print("The deck is out of cards to draw from")
                return
        else:
            print("----------------------")
            print("Your input is invalid")
            print("You lost your turn")
            p1, p2 = p2, p1
            current = (current + 1) % 2
    if len(p1) == 0:
        print("Player 1 Won!")
        print("GAME OVER")
    elif len(p2) == 0:
        print("Player 2 won!")
        print("GAME OVER")

def vaild_play(face_up, card):
    if face_up[0] == card[0] or face_up[1] == card[1]:
        return True
    else: 
        return False

start_game(deck)
