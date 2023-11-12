# Day 5
# Python loops

# Novas funções conhecidas:
# random.choice() - escolhe aleatoriamente um elemento de uma lista
# random.shuffle() - reordena aleatoriamente os elementos de uma lista

# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# Exercício 1
# não usar as funções sum() ou len()
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
number_of_students = 0

for height in student_heights:
  total_height += height
  number_of_students += 1

average_height = round(total_height / number_of_students)

msg = f'''total height = {total_height}
number of students = {number_of_students}
average height = {average_height}
'''
print(msg)

# Exercício 2
# não usar as funções max() ou min()
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = student_scores[0]

for score in student_scores:
   if score > highest_score:
      highest_score = score

print(f"The highest score in the class is: {highest_score}")

# For loop with Range
# for number in range(1, 11, 2):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# Exercício 3
target = int(input("Enter a number between 0 and 1000\n"))
even_sum = 0

for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)

# Exercício 4
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

# Exercício Final
import random 

msg = "Welcome to the PyPassword Generator!\n"
nr_letters = int(input(msg + "How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



#Easy level - Order not randomised:
password = ""

for char in range(0, nr_letters):
#     x = random.randint(0, len(letters) - 1)
#     random_letter = letters[x]
#     password += random_letter
    password += random.choice(letters)
for char in range(0, nr_symbols):
#     random_index = random.randint(0, len(symbols) - 1)
#     random_symbol = symbols[random_index]
#     password += random_symbol
    password += random.choice(symbols)
for char in range(0, nr_numbers):
#     random_index = random.randint(0, len(numbers) - 1)
#     random_number = numbers[random_index]
#     password += random_number
    password += random.choice(numbers)

print(f"Here is your password: {password}")

# Hard level - Order of characters randomised:
password = ""
password_chars = []

for char in range(0, nr_letters):
    password_chars.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_chars.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_chars.append(random.choice(numbers))

# Reordenando os itens de uma lista de forma aleatória
# print(password_chars)
random.shuffle(password_chars)
# print(password_chars)

for char in password_chars:
    password += char

print(f"Here is your password: {password}")