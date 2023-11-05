print("Day 1 - Python Print Function")
print("The function is declared like this:")
print('print("what to print")\n')

#Exercício 1
#Receber um nome qualquer e retornar a quantidade de letras
name = input("Digite um nome:")
print(len(name))

#Exercício 2
#Trocando valores de variáveis
a = int(input("Digite um número:\n"))
b = int(input("Digite um número:\n"))
#Switching
c = a
a = b
b = c
print(f"a: {a}\nb: {b}")

#Como eu fiz:
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print(f"Your band name could be {city_name} {pet_name}")

#Os inputs também podem ficar dentro do print 
#print("Your band name could be " + input("What's the name of the city you grew up in?\n") + " " + input("What's your pet's name?\n"))