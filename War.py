import random
from time import sleep

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]

random.shuffle(deck)

player1_hand = deck[:26]
player2_hand = deck[26:]

def card_comparison(p1_card, p2_card):

    p1_rank = p1_card.split()[0]
    p2_rank = p2_card.split()[0]
    	
    if ranks.index(p1_rank) > ranks.index(p2_rank):
        return 1
    elif ranks.index(p1_rank) < ranks.index(p2_rank):
        return 2
    else:
        return 0
        
def play_round(player1_hand, player2_hand):
    if len(player1_hand) < 5:
        print("Player 1 is about to lose!")
    elif len(player2_hand) < 5:
        print("Player 2 is about to lose!")

    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
       	
    print(f"Player 1 plays: {p1_card}")
    print(f"Player 2 plays: {p2_card}")
    
    result = card_comparison(p1_card, p2_card)
    
    if result == 1:
        print("Player 1 wins the round!")
        player1_hand.extend([p1_card, p2_card])
    elif result == 2:
        print("Player 2 wins the round!")
        player2_hand.extend([p1_card, p2_card])
    else:
        print("WAR!!!!!!!!!!!")
        war_round(player1_hand, player2_hand)

def war_round(player1_hand, player2_hand):
    sleep(0.6)
    if len(player1_hand) < 4:
        player1_hand.clear()
    elif len(player2_hand) < 4:
        player2_hand.clear()
    else:
        p1_card1 = player1_hand.pop(0)
        p2_card1 = player2_hand.pop(0)
        p1_card2 = player1_hand.pop(0)
        p2_card2 = player2_hand.pop(0)
        p1_card3 = player1_hand.pop(0)
        p2_card3 = player2_hand.pop(0)
            
        p1_card4 = player1_hand.pop(0)
        p2_card4 = player2_hand.pop(0)

        war_result = card_comparison(p1_card4, p2_card4)

        if war_result == 1:
            print("Player 1 wins the war!")
            player1_hand.extend([p1_card1, p1_card2, p1_card3, p1_card4, p2_card1, p2_card2, p2_card3, p2_card4])
        elif war_result == 2:
            print("Player 2 wins the war!")
            player2_hand.extend([p1_card1, p1_card2, p1_card3, p1_card4, p2_card1, p2_card2, p2_card3, p2_card4])
        else:
            print("WAR AGAIN !!!!!!")
            war_round(player1_hand, player2_hand)

def play_game():
    round_counter = 0                            
    while (len(player1_hand) > 0 and len(player2_hand) > 0):
        print(f"------ Round {round_counter + 1} ------")
        play_round(player1_hand, player2_hand)
        round_counter += 1
        sleep(0.6)
    if len(player1_hand) == 0:
        print("-----------------------")
        print("Player 2 wins the game!")
        sleep(0.6)
        print("GAME OVER")
    else:
        print("-----------------------")
        print("Player 1 wins the game!")
        sleep(0.6)
        print("GAME OVER")

play_game()
