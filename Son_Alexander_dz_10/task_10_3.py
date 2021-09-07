class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        self.cell += other.cell
        return self.cell

    def __sub__(self, other):
        if self.cell <= other.cell:
            raise Exception(f'Разность этих клеток меньше нуля')
        self.cell -= other.cell
        return self.cell

    def __mul__(self, other):
        self.cell = self.cell * other.cell
        return self.cell

    def __floordiv__(self, other):
        self.cell = self.cell // other.cell
        return self.cell

    def make_order(self, number_of_cells):
        number_full_str = self.cell // number_of_cells
        full_str = '*' * number_of_cells + '\n'
        if self.cell % number_of_cells != 0:
            number_last_str = self.cell % number_of_cells
            last_str = '*' * number_last_str + '\n'
            final_string = full_str * number_full_str + last_str
        else:
            final_string = full_str * number_full_str
        return final_string


cell1 = Cell(12)
cell2 = Cell(23)
print(cell2+cell1)
print(cell1.make_order(4))
print(cell2 .make_order(4))



