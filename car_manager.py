from random import randint as num
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        car = Turtle(shape="square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(COLORS[num(0, len(COLORS)-1)])
        car.up()
        car.setpos(300, num(-250, 250))
        car.setheading(180)
        self.cars.append(car)
    
    def move(self):
        for car in self.cars:
            car.forward(self.speed)
    
    def next_level(self):
        for car in self.cars:
            car.clear()
            self.cars.remove(car)
            car.hideturtle()
        self.speed += MOVE_INCREMENT
