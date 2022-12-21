from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 21, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as files:
            self.high_score = int(files.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score} High Score: {self.high_score}", align=ALIGNMENT, font= FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()





