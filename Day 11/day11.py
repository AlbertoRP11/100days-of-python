import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []


def get_card(cards, hand):
    card = random.choice(cards)
    print(card)
    if get_score(hand) > 10 and card == 11:
        card = 1
    hand.append(card)

def get_score(list_of_cards):
    return sum(list_of_cards)

def show_score():
    print(f"Your cards: {player_cards}, current score: {get_score(player_cards)}")

def final_score():
    print(f"Your final hand: {player_cards}, final score: {get_score(player_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {get_score(computer_cards)}")

def winner_check(hand):
    score = get_score(hand)
    if score == 21:
        final_score()
        if hand == player_cards:
            print("You won")
        else:
            print("You lose!")
        return True
    elif score > 21:
        final_score()
        if hand == computer_cards:
            print("You won")
        else:
            print("You lose!")
        return True
    else:
        return False

def start_hands():
    get_card(cards, player_cards)
    get_card(cards, player_cards)
    get_card(cards, computer_cards)
    print(logo)
    show_score()
    print(f"Computer's first card: {computer_cards[0]}")

def draw():
    get_card(cards, player_cards)
    get_card(cards, computer_cards)
    final_score()
    if computer_cards[-1] > player_cards[-1]:
        print("You won")
    else:
        print("You lose!")

def players_turn():
    should_continue = True
    while should_continue:
        want_cards = input("Type 'y' to get another card, type 'n' to pass:")
        if want_cards == "y":
            get_card(cards, player_cards)
            winner = winner_check(player_cards)
            if not winner:
                show_score()
            else:
                final_score()
                should_continue = False
        else:
            should_continue = False

def computers_turn():
    should_continue = True
    while should_continue:
        get_card(cards, computer_cards)
        winner_check(computer_cards)
        computer_score = get_score(computer_cards)
        player_score = get_score(player_cards)
        if computer_score > player_score and computer_score <= 21:
            final_score()
            print("You lose!")
            should_continue = False
        elif computer_score <= player_score and computer_score < 21:
            should_continue = True
        elif computer_score == player_score:
            draw()
            should_continue = False
        elif computer_score > 21:
            final_score()
            print("You won!")
            should_continue = False


def play():
    start_hands()
    winner = winner_check(player_cards)
    if not winner:
        players_turn()
        computers_turn()

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if want_to_play == "y":
    play()