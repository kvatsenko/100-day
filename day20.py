import turtle as t
import time
from turtle import Screen, Turtle
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.down,"Down")


game_on=True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on=False
        scoreboard.game_off()

    for seg in snake.turtles:

        if seg==snake.head:
            pass

        elif snake.head.distance(seg) < 10:
            game_on=False
            scoreboard.game_off()

my_screen.exitonclick()