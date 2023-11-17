# Day 13
# Debugging: How to Find and Fix Errors in your Code

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20: bug here -> i never turns into 20
#       print("You got it")
# my_function()
def my_function():
  for i in range(1, 21): #change the range to make the code work
    if i == 20: 
      print("You got it")
my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) bug here -> it will cause an out of range error
# print(dice_imgs[dice_num]) because it will be used as an index here
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # now the code works properly
print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: bug here -> the year 1994 is not included in any of the statements
#   print("You are a millenial.")
# elif year > 1994: bug here -> the year 1994 is not included in any of the statements
#   print("You are a Gen Z.")
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994: # now 1994 is included here
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") bug here -> didn't cast age
# if age > 18:
# print("You can drive at age {age}.") bug here -> not indented and forgot the f to format the text
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # bug here -> we're comparing two things
# total_words = pages * word_per_page
# print(total_words)
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) bug here -> not indented
#   print(b_list)

# mutate([1,2,3,5,8,13])
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# Which number do you want to check?
# number = int(input())

# if number % 2 = 0: bug here -> we're not comparing
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
number = int(input())

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# year = input("Which year do you want to check?") bug here -> not casted
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
year = int(input("Which year do you want to check?")) 
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# Target is the number up to which we count
# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 or number % 5 == 0: bug here
#     print("FizzBuzz")
#   if number % 3 == 0: bug here
#     print("Fizz")
#   if number % 5 == 0: bug here
#     print("Buzz")
#   else:
#     print([number]) error here
target = int(input("Target"))
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)