from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.set_score()

    def set_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {str(self.score)}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over\nFinal Score: {str(self.score)}", align="center", font=FONT)

    def level_complete(self, level):
        self.clear()
        self.score += 1
        self.goto(0, 0)
        self.write(f"Level Complete\nNext level: {str(level)}", align="center", font=FONT)

    def game_won(self):
        self.clear()
        self.goto(0, 0)
        self.write("Congratulations! You Won!", align="center", font=FONT)