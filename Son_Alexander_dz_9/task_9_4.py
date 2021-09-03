class Car:
    def __init__(self, speed, color, name, is_police, move, turn):
        self.speed = speed
        self.colour = color
        self.name = name
        self.is_police = is_police
        self.turn = turn

    def go(self):
        return ('Машина поехала')

    def stop(self):
        return ('Машина остановилась')

    def turn(self, direction):
        return (f'Машина повернула на {direction}')


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
print(honda.show_speed(), honda.go())


