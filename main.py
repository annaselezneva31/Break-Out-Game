from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=650)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

scoreboard = Scoreboard()
paddle = Paddle()
bricks = Bricks()
current_bricks = bricks.bricks_list
ball = Ball()
ball.goto_paddle((paddle.xcor(), paddle.ycor()+20))

screen.listen()
screen.onkey(paddle.left_move, "Left")
screen.onkey(paddle.right_move, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    if scoreboard.lives > 0 and scoreboard.score_player != 60:
        if ball.is_collision_side_wall():
            ball.change_x()
        if ball.is_collision_upper_wall():
            ball.change_y()
        if ball.is_collision_paddle(paddle):
            ball.change_y()
        if ball.is_collision_down_wall():
            ball.goto_paddle((paddle.xcor(), paddle.ycor()+20))
            scoreboard.lives_down()
        for brick in current_bricks:
            if ball.is_collision_bricks(current_bricks[brick]):
                ball.change_y()
                current_bricks[brick].hideturtle()
                current_bricks.pop(brick)
                scoreboard.score_up()
                if scoreboard.score_player % 5 == 0:
                    ball.move_speed *= 0.85
                break
    else:
        game_is_on = False
        scoreboard.game_over()
    screen.update()

screen.exitonclick()