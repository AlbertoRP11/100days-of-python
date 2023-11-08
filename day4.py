# Day 4
# Randomisation and python lists

import random
# import module4
# print(module4.pi)

# random_integer = random.randint(1, 10)
# print(random_integer)

#0.0000000 - 0.9999999...
# random_float = random.random()*5
# print(random_float)

# Exercício 1
# random_side = random.randint(0, 1)
# print(random_side)

# Lists
states_of_usa = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# states_of_usa[-1] = "Avaí"
# states_of_usa.append("São Paulo")
# states_of_usa.extend(["Rio de Janeiro", "Minas Gerais"])
print(states_of_usa)


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

# Exercício 2 
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")
# The input pattern it's like "B3"
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)

number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")

# Exercício Final
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Não tinha pensado em usar lista pra dar match com a escolha
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose:\n" + game_images[computer_choice])


    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == 0:
        if computer_choice == 1:
            print("You lose")
        elif computer_choice == 2:
            print("You won")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You won")
        elif computer_choice == 2:
            print("You lose")
    else:
        if computer_choice == 0:
            print("You lose")
        elif computer_choice == 1:
            print("You won")

# Outra maneira de checar seria essa:
# if user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")