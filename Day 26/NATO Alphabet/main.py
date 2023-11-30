import pandas as pd

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in df.iterrows():
#     nato_dict[row.letter] = row.code
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Whats your word?").upper()
# name_letters = [char for char in word]
# nato_word = [code for (letter, code) in nato_dict.items() if letter in name_letters]
nato_word = [nato_dict[letter] for letter in word]
print(nato_word)
