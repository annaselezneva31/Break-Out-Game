from turtle import Turtle

AL_RIGHT = "right"
AL_CENTER = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_player = 0
        self.lives = 3
        self.goto(370, 270)
        self.write(f"Lives: {self.lives}\n"
                   f"Score: {self.score_player}", False, AL_RIGHT, FONT)

    def score_up(self):
        self.score_player += 1
        self.clear()
        self.write(f"Lives: {self.lives}\n"
                   f"Score: {self.score_player}", False, AL_RIGHT, FONT)

    def lives_down(self):
        self.lives -= 1
        self.clear()
        self.write(f"Lives: {self.lives}\n"
                   f"Score: {self.score_player}", False, AL_RIGHT, FONT)

    def game_over(self):
        self.goto(0,25)
        self.write("GAME OVER", False, AL_CENTER, FONT)
        self.goto(0, -25)
        if self.lives > 0:
            self.write("You won!", False, AL_CENTER, FONT)
        else:
            self.write("You lost!", False, AL_CENTER, FONT)