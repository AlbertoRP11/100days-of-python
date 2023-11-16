# Day 12
# Scope and Number Guessing Game

# Number Guessing Game
import random
from art import logo 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def start():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking in a number between 1 and 100")
    secret_number = random.randint(0, 100)
    # print(secret_number)
    return secret_number

def choose_difficulty():
    difficulty = input("Choose a difficulty level.\nType 'easy' or 'hard':")
    return difficulty

def compare(guess, number):
    if guess != number:
        if guess > number:
            print("Too high!\nGuess again.")
        else:
            print("Too low!\nGuess again.")
    else:
        print(f"You got it! The answer is {number}.")

def game(number, total_guesses):
    guess = 0
    while total_guesses > 0 and guess != number:
        print(f"You have {total_guesses} attemps remaining to guess the number.")
        guess = int(input("Guess a number:"))
        total_guesses -= 1
        if total_guesses == 0 and guess != number:
            print("You ran out of guesses. You lose!")
            print(f"The secret number was {number}.")
        else:
            compare(guess, number)

def play(difficulty, number):
    if difficulty == "easy":
        total_guesses = EASY_LEVEL_TURNS
    elif difficulty == "hard":
        total_guesses = HARD_LEVEL_TURNS
    game(number, total_guesses)

def main():
    secret_number = start()
    difficulty_level = choose_difficulty()
    play(difficulty_level, secret_number)

main()

# Local Scope:
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
# print(potion_strength) NameError - "potion_strength" is only acessible in the function scope

# Global Scope:
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()
# print(player_health)

# There's no Block Scope:
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0] # this doesn't count as a local scope just because it's inside an if statement
# print(new_enemy) # basically, only functions create a local scope (if, while, for don't)

# Modifying Global Scope:
# enemies = 1

# def increase_enemies():
# #   global enemies - we usually don't modify global variables
# #   enemies += 1
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# x = increase_enemies()
# print(f"Retorno da função: {x}")
# print(f"enemies outside function: {enemies}")

# But it's not true we should never use global scope
# It's very usefull when we're creating constants
# The convention is to name the constants all uppercase separeted by underscore so we remember to not modify them

# Global constants 
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "peruchi_alberto"