# Day 7
# Hangman Game

import random
from hangman_art import stages, logo
from hangman_words import word_list

# logo = hangman_art.logo
# stages = hangman_art.stages
# word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append("_") 
# poderia ser display += "_"

end_of_game = False
lives = 6

print(logo)

#Testando 
print(chosen_word)

guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    guessed_letters += guess

# Fiz o programa checando se a letra já foi um "guess" antes, independente de estar na palavra escolhida ou não
# Por isso essa nova variável "guessed_letters"
# Caso fizesse apenas checando se uma letra que faz parte da palavra escolhida está sendo digitada novamente
# Poderia ser feito por -> if guess in display
    if guessed_letters.count(guess) > 1:
        print(f"You've already guessed {guess}")
    else:
      for position in range(len(chosen_word)):
          if chosen_word[position] == guess:
              display[position] = guess


      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}\n")
      
      if guess not in chosen_word:
          print(f"You guessed {guess}, that's not in the word. You lose a life.")
          lives -= 1
          if lives == 0:
              print("You lose!")
              end_of_game = True

      if "_" not in display:
          end_of_game = True
          print("You win!")

      print(stages[lives])