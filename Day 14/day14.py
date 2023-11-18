import random

from art import logo, vs
from game_data import data

# Get data:
def get_item():
    index = random.randint(0, len(data) - 1)
    item = data[index]
    return item

def diff_items(item_A, item_B):
    while item_A == item_B:
        item_B = get_item()
    return item_B

def compare(item_A, item_B):
    print(f"Compare A: {item_A['name']}, {item_A['description']} from {item_A['country']}.")
    # print(f"{item_A['follower_count']}") - testing code
    print(vs)
    print(f"Against B: {item_B['name']}, {item_B['description']} from {item_B['country']}.")
    # print(f"{item_B['follower_count']}") - testing code
    if item_A["follower_count"] > item_B["follower_count"]:
        return "a"
    else:
        return "b"

def user_guess():
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    if guess == "a" or guess == "b":
        return guess
    else:
        print("Select a valid option!")
        user_guess()

def continue_game(last_celeb, score):
    should_continue = True
    while should_continue:
        celeb_A = last_celeb
        celeb_B = get_item()
        more_followers = compare(celeb_A, celeb_B)
        guess = user_guess()
        if guess == more_followers:
            last_celeb = celeb_B
            score += 1
            print(f"You're right! Current score: {score}.")
            should_continue = True
        else: 
            should_continue = False
    return score

def start_game():
    print(logo)
    score = 0
    celeb_A = get_item()
    celeb_B = get_item()
    celeb_B = diff_items(celeb_A, celeb_B)
    more_followers = compare(celeb_A, celeb_B)
    guess = user_guess()
    if guess == more_followers:
        score += 1
        print(f"You're right! Current score: {score}.")
        score = continue_game(celeb_B, score)
    print(f"Sorry, that's wrong. Final score: {score}")

start_game()