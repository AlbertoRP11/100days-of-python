# import colorgram
import random
import turtle as t

# Extracting colors from an image.
# colors = colorgram.extract('hirst-1.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

tom = t.Turtle()
t.colormode(255)
tom.speed("fast")
tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)

for _ in range(10):
    for _ in range(10):
        tom.dot(20, random.choice(color_list))
        tom.forward(50)
    tom.left(90)
    tom.forward(50)
    tom.left(90)
    tom.forward(500)
    tom.right(180)

screen = t.Screen()
screen.exitonclick()
