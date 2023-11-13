# Day 8
# Function Parameters & Caesar Cipher

# Exercício Final 
# Caesar Cipher
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    modified_text = ""

    for char in text:
        if char not in alphabet:
            new_char = char
        else:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = position + shift
                if new_position >= len(alphabet):
                    new_position -= 26
            elif direction == "decode":
                new_position = position - shift
                if new_position < 0:
                    new_position += 26 
            new_char = alphabet[new_position]
        modified_text += new_char
    
    print(f"\nThe {direction}d text is {modified_text}.")

should_end = False
while not should_end:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet):
        shift %= 26

    caesar(text, shift, direction)

    restart = input("Do you want to coninue?\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye!")

# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#     print("Hello")
#     print("Welcome to the Greet Function")
#     print("Bye!")

# greet()

# Functions with inputs
# def greet_with_name(name):
#     print(f"Hello, {name}")
#     print(f"Welcome to the Greet Function")
#     print(f"Bye, {name}!")

# name=parameter  "Alberto"=argument
# greet_with_name("Alberto")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"Isnt't the weather nice today in {location}?")

# Positional Arguments -> name="Alberto", location="São Paulo"
# greet_with("São Paulo", "Alberto") then name="São Paulo" and location="Alberto"
#greet_with("Alberto", "São Paulo")

# Keyword Argumnets -> switching the order doesn't affect the code because you're defining which parameter each argument is referring to
#greet_with(location="São Paulo", name="Alberto")

# Exercício 1
# Paint Calculator

# import math
# def paint_calc(height, width, cover):
#     num_cans = (height * width) / cover
#     # math.ceil() rounds up a number
#     print(f"You'll need {math.ceil(num_cans)} cans of paint.")
# test_h = int(input("Height of wall (m):"))
# test_w = int(input("Width of wall (m):"))
# coverage = 5

# paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercício 2
# Prime Numbers

# def prime_checker(number):
#     if number == 2 or number == 3 or number == 5 or number == 7:
#         prime = True
#     elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
#         prime = False
#     else:
#         prime = True
    
#     if prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# prime_checker(5)

# Other solution:
# def prime_checker(number):
#     is_prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# Exercício Final
# Caesar Cipher

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         # getting the letter index on the alphabet
#         index = alphabet.index(letter)
#         if index + shift > len(alphabet) - 1:
#             cipher_text += alphabet[(index + shift) - 26]
#         else:
#             #shifting the letter using the index and the shift wanted
#             cipher_text += alphabet[index + shift]
#     print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#     decrypted_text = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         if index - shift < 0:
#             decrypted_text += alphabet[(index - shift) + 26]
#         else:
#             decrypted_text += alphabet[index - shift]
#     print(f"The decoded text is {decrypted_text}")