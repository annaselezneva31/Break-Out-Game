from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def goto_paddle(self, position):
        self.goto(position)

    def is_collision_paddle(self, paddle):
        is_collision = False
        if -300 < self.ycor() < -285 and paddle.xcor() - 80 < self.xcor() < paddle.xcor() + 80:
            is_collision = True
        return is_collision

    def is_collision_side_wall(self):
        is_collision = False
        if self.xcor() > 375 or self.xcor() < -380:
            is_collision = True
        return is_collision

    def is_collision_upper_wall(self):
        is_collision = False
        if self.ycor() > 320:
            is_collision = True
        return is_collision

    def is_collision_down_wall(self):
        is_collision = False
        if self.ycor() < -320:
            is_collision = True
        return is_collision

    def is_collision_bricks(self, brick):
        is_collision = False
        if self.distance(brick) < 30:
            is_collision = True
        return is_collision

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def change_y(self):
        self.y_move *= -1

    def change_x(self):
        self.x_move *= -1
