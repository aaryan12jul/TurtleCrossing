from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.up()
        self.setpos(STARTING_POSITION)
        self.setheading(90)
    
    def moveUp(self):
        self.forward(MOVE_DISTANCE)
        
    def is_at_finishline(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
            return True
        else:
            return False