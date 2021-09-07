class Matrix:
    def __init__(self, list_Of_List):
        self.matrix = list_Of_List
        listsLen = len(list_Of_List[0])
        for _list in self.matrix:
            if len(_list) != listsLen:
                raise Exception(f'__init__: Списки должны быть одинаковой длины')

    def __str__(self):
        matrix_str = ''
        for _list in self.matrix:
            _list = [str(value) for value in _list]
            matrix_str += '   '.join(_list) + '\n'
        return matrix_str

    def __add__(self, other):
        if len(other.matrix) == len(self.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            i = -1
            for list_1, list_2 in zip(self.matrix, other.matrix):
                i += 1
                sum_list = []
                for value_1, value_2 in zip(list_1, list_2):
                    sum_list.append(value_1 + value_2)
                self.matrix[i] = sum_list
            return self
        else:
            return f'__add__: Матрицы невозможно сложить'


matrix1 = Matrix([[2, 3], [3, 4], [5, 6]])
print(matrix1)
matrix2 = Matrix([[2, 3], [3, 4], [5, 6]])
print(matrix1 + matrix2)
