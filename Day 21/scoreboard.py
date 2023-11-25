from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
