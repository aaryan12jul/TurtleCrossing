from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.level = 1
        self.up()
        self.setpos(-200, 230)
        self.hideturtle()
        self.color("black")
        self.write(f"Level: {self.level}", True, align="center", font=FONT)
    
    def update(self):
        self.clear()
        self.level += 1
        self.setpos(-200, 230)
        self.write(f"Level: {self.level}", True, align="center", font=FONT)
    
    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game Over", True, align="center", font=FONT)