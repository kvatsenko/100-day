import turtle as t 
from turtle import Turtle, Screen
import random

start = Turtle()
my_screen = Screen()


# def forward():
#     timmy.forward(10)

# def back():
#     timmy.backward(10)
# def left():
#     timmy.left(30)
# def right():
#     timmy.right(30)
    
# def clear():
#     timmy.clear()

# my_screen.onkey(key="w", fun=forward)
# my_screen.onkey(key="s", fun=back)
# my_screen.onkey(key="a", fun=left)
# my_screen.onkey(key="d", fun=right)
# my_screen.onkey(key="c", fun=clear)
#my_screen.listen()

start.shape("turtle")
start.color("gray")

colors=["red", "green", "black"]
move=[0,20,40]
all_turtles=[]


start.pencolor("white")
start.forward(300)
start.left(90)
start.pencolor("black")
start.forward(50)
start.backward(70)


for i in range(0,3):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
    new_turtle.left(90)
    new_turtle.fd(move[i])
    new_turtle.left(90)
    new_turtle.fd(200)
    new_turtle.right(180)

gues=my_screen.textinput("Gues", "what turtle are you bet on?")


if gues:
    rase_true=True

while rase_true:
    for turtle in all_turtles:
        if turtle.xcor()>300:
            rase_true=False
            winer=turtle.pencolor()
            if winer==gues:
                print(f"you win! {winer} turtle has won!")
            else:
                print(f"you lose! {winer} turtle has won!")
            
        distanse=random.randint(0,10)
        turtle.forward(distanse)
    




my_screen.exitonclick()

# lol={"red":"me"}

# # if lol["red"]=="me":
# #     print("yep")

# print(lol["red"])