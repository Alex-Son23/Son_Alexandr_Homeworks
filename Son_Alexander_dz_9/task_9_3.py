class Worker:
    def __init__(self, name, surname, position, *income):
        self.name = name
        self.surname = surname
        self.position = position
        if len(income) > 1:
            self._income = {'wage': income[0], 'bonus': income[1]}
        else:
            self._income = {'wage': income[0]}

class Position(Worker):
    def get_full_name(self):
        fullname = f'{self.name} {self.surname}'
        return fullname
    def get_total_income(self):
        total_income = 0
        for key, income in self._income.items():
            total_income += income
        return total_income


me = Worker('Alex', 'Son', 'programmer', 132234234, 231242)
i_am = Position('Alex', 'Son', 'programmer', 132234234, 231242)

print(me._income, me.name, me.surname, me.position)
print(i_am.get_total_income(), i_am.get_full_name())
