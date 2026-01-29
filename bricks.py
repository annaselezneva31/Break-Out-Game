from turtle import Turtle
from brick import Brick

class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.bricks_list = {}
        self.create_bricks()

    def create_bricks(self):
        colors = ["red", "orange", "green", "blue"]
        y = 280
        for j in range(4):
            x = -355
            y -= 30
            for i in range(15):
                brick = Brick((x, y), colors[j])
                self.bricks_list[f"{j+1}-{i+1}"] = brick
                x += 50
