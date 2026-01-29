from turtle import Turtle

START_POSITION = (0, -300)

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=8)
        self.color("white")
        self.penup()
        self.goto(START_POSITION)

    def left_move(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def right_move(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())