from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=FONT)
