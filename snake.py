from turtle import Turtle
MOVE_DISTACE=20
START_POSITION=[(0,0),(-20,0),(-40,0)]
UP = 90
LEFT = 180
RIGHT = 0 
DOWN = 270

class Snake:
    def __init__(self):
        self.turtles =[]
        self.create_snake()
        self.head = self.turtles[0]


    def create_snake(self):
        for position in START_POSITION:
            self.add_segment_of_snake(position)


    def add_segment_of_snake(self, position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_segment_of_snake(self.turtles[-1].position())

    def move(self):
        for seg_num in range(len(self.turtles)-1, 0, -1):
            new_x=self.turtles[seg_num - 1].xcor()
            new_y=self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTACE)

    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



# def move():
#     if head.direction == "up":
#         y = head.ycor()
#         head.sety(y+20)
#     if head.direction == "dowind":
#         y = head.ycor()
#         head.sety(y-20)
#     if head.direction == "left":
#         x = head.xcor()
#         head.setx(x-20)
#     if head.direction == "right":
#         x = head.xcor()
#         head.setx(x+20)
 
# wind.listen()
# wind.onkeypress(group, "w")
# wind.onkeypress(godowind, "s")
# wind.onkeypress(goleft, "a")
# wind.onkeypress(goright, "d")
