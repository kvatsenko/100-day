import turtle as t 
from turtle import Turtle, Screen
import random
timmy = Turtle()

timmy.shape("turtle")
timmy.color("black", "gray")
# timmy.forward(100)

# while True:
#     timmy.forward(100)
#     timmy.left(90)
#     if abs(timmy.pos()) < 1:
#         break


# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# while True:



# list=[
#       {"collor":"black", "sides": 3}, 
#       {"collor":"red", "sides": 4}, 
#       {"collor":"blue", "sides": 5}, 
#       {"collor":"green", "sides": 6}, 
#       {"collor":"yellow", "sides": 8}
#       ]

# def shape():
#     for i in list:
#         for y in range(0, i["sides"]):
#             timmy.pencolor(i["collor"])
#             timmy.forward(100)
#             timmy.left(360/i["sides"])

# shape()

# list=["yellow", "black", "purple", "red", "blue", "green"]

# move_degree=[0, 90, 180, 270]
# timmy.pensize(7)
# t.colormode(255)
# timmy.speed("fastest")




# def move():
#     for i in range(0, 1000):
#         timmy.color(random_color())
#         timmy.right(random.choice(move_degree))
#         timmy.forward(10)

# move()

import colorgram

# timmy.speed("fastest")
# # while True:
# #     timmy.forward(200)
# #     timmy.left(170)
# #     if abs(timmy.pos()) < 1:
# #         break
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     r_c=(r, g, b)
#     return r_c

# for i in range(72):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.left(5)


# import colorgram
# colors = colorgram.extract('image.jpg', 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

t.colormode(255)
color_list=[(246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), 
            (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), 
            (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), 
            (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), 
            (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), 
            (168, 99, 102)]
timmy.color("white")
timmy.goto(300, 300)
timmy.left(180)
timmy.speed("fastest")
timmy.penup()


def left():
    for i in range(13):
        timmy.dot(20, random.choice(color_list))
        timmy.fd(50)

    timmy.left(90)
    timmy.fd(50)
    timmy.left(90)
    timmy.fd(50)

def right():
    for i in range(13):
        timmy.dot(20, random.choice(color_list))
        timmy.fd(50)

    timmy.right(90)
    timmy.fd(50)
    timmy.right(90)
    timmy.fd(50)

for n in range(7):
    left()
    right()


my_screen = Screen()
my_screen.exitonclick()
