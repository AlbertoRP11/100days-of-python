import turtle

import pandas
import pandas as pd

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE)

turtle.shape(IMAGE)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
correct_guesses = []

while len(correct_guesses) < len(states):
    guess = screen.textinput(title=f"{len(correct_guesses)}/{len(states)} Guess the State",
                             prompt="Guess a state's name").title()
    if guess == "Exit":
        missing_states = []
        for state in states:
            if state not in correct_guesses:
                missing_states.append(state)
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if guess in states:
        correct_guesses.append(guess)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        correct_state = data[data.state == guess]
        text.goto(int(correct_state.x.item()), int(correct_state.y.item()))
        text.write(guess)

screen.exitonclick()
