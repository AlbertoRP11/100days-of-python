# Mail Merger

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    invites_list = []
    for line in file.readlines():
        name = line.strip("\n")
        invites_list.append(name)

with open("./Input/Letters/starting_letter.txt") as file:
    invite_model = file.read()

for name in invites_list:
    with open(f"./Output/ReadyToSend/{name}_invite.txt", mode="w") as file:
        personalized_invite = invite_model.replace(PLACEHOLDER, name)
        file.write(personalized_invite)
