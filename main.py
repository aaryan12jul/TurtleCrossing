import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.moveUp)

add_cars = 10
while True:
    for i in range(add_cars):
        time.sleep(0.1)
        car.move()
        
        if player.is_at_finishline():
            car.next_level()
            scoreboard.update()
            add_cars -= 1
            if add_cars <= 0:
                add_cars = 1

        for vehiciles in car.cars:
            if player.distance(vehiciles) < 30:
                screen.update()
                scoreboard.game_over()
                break
        else:
            screen.update()
            continue
        break
    else:
        car.create_car()
        continue
    screen.update()
    break

screen.exitonclick()