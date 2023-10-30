from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0,280)
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 15, 'normal'))
    
    def game_off(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=('Arial', 30, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
