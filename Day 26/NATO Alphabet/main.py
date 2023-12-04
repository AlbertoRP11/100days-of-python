import pandas as pd

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in df.iterrows():
#     nato_dict[row.letter] = row.code
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Whats your word?").upper()
    try:
        nato_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please")
        generate_phonetic()
    else:
        print(nato_word)

generate_phonetic()
