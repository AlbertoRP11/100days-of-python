# Day 3
# Control flow and logical operators

# Exercício 1
print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?\n"))

if (height > 120):
    print("You can ride the rollercoaster!")
    age = int(input("What's your age?\n"))
    if (age < 12):
        print("Please pay $5.")
    elif (age <= 18):
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Exercício 2
year = int(input("Which year do you want to check?\n"))
if (year % 4 == 0):
  if (year % 100 == 0):
    if (year % 400 == 0):
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

# If/elif/else:
# No caso abaixo, apenas uma das operações (A, B ou C) será feita
# if (condition1):
#     do A
# elif (condition2):
#     do B
# else:
#     do C

# Multiple if:
# Já aqui, todas as operações (A, B, C) podem ocorrer, desde que satisfaçam as condições (1, 2, 3)
# if (condition1):
#     do A
# if (condition2):
#     do B
# if (condition3):
#     do C

# Exercício 3
print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?\n"))
bill = 0

if (height > 120):
    print("You can ride the rollercoaster!")
    age = int(input("What's your age?\n"))
    if (age < 12):
        bill = 5
        print("Child tickets are $5.")
    elif (age <= 18):
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want photos taken? Y or N\n")
    if (wants_photo == "Y"):
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Exercício 4
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0 

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

# Exercício 5
name1 = input("What's your name?\n")
name2 = input("What's your partner's name?\n")
# name1 = name1.lower()
# name2 = name2.lower()
combined_names = name1 + name2
combined_names = combined_names.lower()

first_digit = 0
first_digit += combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
first_digit = str(first_digit)
second_digit = 0
second_digit += combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")
second_digit = str(second_digit)

love_score = int(first_digit+second_digit)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

# Exercício Final
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input('You\'re at a cross road. Which way do you want to go? Type "left" or "right"\n').lower() #\ permite fazer a formatação como queremos
if direction == "left":
    decision = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if decision == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if color == "yellow":
            print("You found the treasure! You Win!")
        elif color == "blue":
            print("You enter a room of beasts. Game Over.")
        elif color == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
