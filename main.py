# IMPORTS
import random
from art import logo

# IMPORTANT DATA, CARD SET
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# BASE VARIABLES
win_condition = False
restart_value = "n"


# FUNCTIONS
def restart_game():
    restart_func_value = input("\nDo you want to restart? (y/n): ")
    if restart_func_value == "n":
        return False
    else:
        return True


def player_draw_card():
    player_cards.append(random.choice(cards))


def dealer_draw_card():
    dealer_cards.append(random.choice(cards))


def cps():
    return sum(player_cards)


def cds():
    return sum(dealer_cards)


def check_player_score(score):
    if score > 21:
        print("\nPS > 21")
        print(f"\nYOU LOSE! Your score: {player_score} with cards: {player_cards}")
        print(f"\nDealers score: {dealer_score} dealers hand: {dealer_cards}")
        return True


def check_dealer_score(score):
    if score > 21:
        print("\nDS > 21")
        print(f"\nYOU WIN! Your score: {player_score} with cards: {player_cards}")
        print(f"\nDealers score: {dealer_score} with cards: {dealer_cards}")
        return True


def check_blackjack():
    if len(dealer_cards) == 2 and sum(dealer_cards) == 21:
        print("\nDS == BLACKJACK")
        print(f"\nYOU LOSE! Your score: {player_score} with cards: {player_cards}")
        print(f"\nDealers score: {dealer_score} dealers hand: {dealer_cards}")
        return True
    if len(player_cards) == 2 and sum(player_cards) == 21:
        print("\nPS == BLACKJACK")
        print(f"\nYOU WIN! Your score: {player_score} with cards: {player_cards}")
        print(f"\nDealers score: {dealer_score} dealers hand: {dealer_cards}")
        return True


def ace_value():
    if 11 in player_cards and player_score > 21:
        player_cards.remove(11)
        player_cards.append(1)
        print("Player ACE value changed to 1")
    if 11 in dealer_cards and dealer_score > 21:
        dealer_cards.remove(11)
        dealer_cards.append(1)
        print("Dealer ACE value changed to 1")


def check_result():
    if player_score == dealer_score:
        print("\nPS == DS")
        print(f"\nDRAW! Your score: {player_score} with cards: {player_cards}")
        print(f"\nDealers score: {dealer_score} with cards: {dealer_cards}")
    if player_score > dealer_score:
        print("\nPS > DS")
        print(f"\nYOU WIN! Your score: {player_score} with cards: {player_cards}")
        print(f"\nDealers score: {dealer_score} with cards: {dealer_cards}")
    if dealer_score > player_score:
        print("\nDS > PS")
        print(f"\nYOU LOSE! Your score: {player_score} with cards: {player_cards}")
        print(f"\nDealers score: {dealer_score} dealers hand: {dealer_cards}")


# --------------------------------------------------------------------------------------------
# START OF GAME
print("\n"*20)
play = input("Do you want to play blackjack? (y/n): ")
while play == "y":

    player_cards = [0]
    player_score = 0
    dealer_cards = [0]
    dealer_score = 0
    win_condition = False
    restart_value = "n"

    # UX
    print("\n" * 50)
    print(logo)

    # DEAL CARDS
    for i in range(2):
        player_cards.append(random.choice(cards))
    for k in range(1):
        player_cards.pop(0)
    for j in range(2):
        dealer_cards.append(random.choice(cards))
    for m in range(1):
        dealer_cards.pop(0)

    dealer_hand = dealer_cards[0]

# MAIN LOOP
    while True:

        restart = "n"

        player_score = cps()
        dealer_score = cds()
        if check_blackjack():
            win_condition = True
            break

        print(f"\nThe dealers first card -> {dealer_hand}")
        print(f"\nYour score: {player_score} with cards: {player_cards}")

        draw_card = input("\nDo you want to draw another card? (y/n): ")

        if draw_card == "y":
            player_draw_card()
            ace_value()
            player_score = cps()
            if check_player_score(player_score):
                win_condition = True
                break
            continue
        else:
            if dealer_score < 16:
                dealer_draw_card()
                ace_value()
                dealer_score = cds()
                if check_dealer_score(dealer_score):
                    win_condition = True
                    break
                if win_condition:
                    break
                else:
                    continue
            break
    if not win_condition:
        check_result()

    if restart_game():
        continue
    else:
        print("(no restart)")
        break

print("End of program")
