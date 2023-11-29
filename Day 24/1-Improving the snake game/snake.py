from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.body.append(new_square)

    def reset(self):
        for segment in self.body:
            segment.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def extend(self):
        # add a new segment to the snake body
        self.add_segment(self.body[-1].position())

    def move(self):
        # Move the blocks of the snake to the position of the blocks right in front of them
        for index in range(len(self.body) - 1, 0, -1):  # start= len(self.body) - 1, stop= 0, step= -1
            new_x = self.body[index - 1].xcor()
            new_y = self.body[index - 1].ycor()
            self.body[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
