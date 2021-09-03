class Stationery:
    def __init__(self):
        self.title = self

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки PEN'


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки PENCIL'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки HANDLE'


pen = Pen()
print(pen.draw())

pencil = Pencil()
print(pencil.draw())

handle = Handle()
print(handle.draw())

