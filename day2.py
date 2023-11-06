#len(12)
#object of type 'int' has no len()

#Data Types

#String
print("hello"[3])
print("123"+"456")

#Integer
print(123 + 456)
print(123_456_789)

#Float
3.14159

#Boolean
True
False

num_char = len(input("What's your name?\n"))
#print("Your name have " + num_char + "characters.")
#TypeError: can only concatenate str (not "int") to str
num_char = str(num_char)
print("Your name have " + num_char + " characters.")

#Data Casting
a = float(123)
print(type(a))

print(70+float("30"))
print(str(70)+str(30))

#Exercício 1
#Input = 39 -> Output = 12
two_digit_number = input()
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit)

3 + 5 # = 8
7 - 4 # = 3
3 * 2 # = 6
6 / 3 # = 2.0, always a float
print(2 ** 3) # 8

print(8 / 3)
print(int(8 / 3)) 
print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)

#f-Strings
score = 1
height = 1.8
is_winning = True

print(f"your score is {score}, your height is {height}, you are winnig is {is_winning}")

#Exercício Final
msg = "Welcome to the tip calculator.\n"
total_bill = float(input(msg + "What was the total bill? \n$"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, 15?\n"))/100
people_spliting = int(input("How many people to split the bill?"))
splitted_bill = (total_bill + (total_bill*percentage_tip))/people_spliting 

print(total_bill)
print(percentage_tip)
print(people_spliting)
print(f"Each person should pay: ${splitted_bill:.2f}")