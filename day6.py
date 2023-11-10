# Day 6
# Python functions & Karel

# Estrutura de uma função:
# def my_function():
#     Do this
#     Then do this
#     Finally do this

# While Loop
# while something_is_true:
#     Do something repeatedly
# Diferentemente do For Loop, com o While precisamos nos preocupar em tornar a condição falsa para que não tenhamos um loop infinito

# For Loop
# for item in list_of_items:
#     Do something to each item

# for number in range(a, b):
#     print(number)

# Os exercícios do dia foram no Reeborg's World
# Hurdle 1, Hurdle 2, Hurdle 3, Hurdle 4 e Maze resolvidos

# Hurdle 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for step in range(0, 6):
#     jump()

# Hurdle 2
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     jump()

# Hurdle 3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()

# Hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     ups = 0
#     while not right_is_clear():
#         move()
#         ups += 1
#     turn_right()
#     move()
#     turn_right()         outra opção seria o seguinte:
#     while ups > 0:       while front_is_clear():
#         move()               move()
#         ups -= 1         turn_left()
#     turn_left()          
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()


# Maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear() == True:
#     move()
# turn_left()
    
# while not at_goal():
#     if not wall_on_right():
#             turn_right()
#             move()
#     elif front_is_clear() == True:
#         move()
#     else:
#         turn_left()