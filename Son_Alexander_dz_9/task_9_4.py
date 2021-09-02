class Car:
    def __init__(self, speed, color, name, is_police, move, turn):
        self.speed = speed
        self.colour = color
        self.name = name
        self.is_police = is_police
        if move is True:
            self.go = True
        else:
            self.stop = True
        self.turn = turn


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Скорость превышена'
        else:
            return self.speed


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Скорость превышена'
        else:
            return self.speed


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


honda = TownCar(70, 'red', 'Black Mamba', True, True, 'Right')
print(honda.show_speed())


