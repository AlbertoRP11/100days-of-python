from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def reached_finish(self):
        if self.ycor() > 280:
            self.go_to_start()
            return True
        else:
            return False
