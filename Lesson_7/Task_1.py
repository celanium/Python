'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы. Примеры матриц: см. в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.'''


class Matrix:
    def __init__(self, rows):
        self.matrix = rows

    def get_rows(self):
        return len(self.matrix)

    def get_columns(self):
        return len(self.matrix[0])

    def __add__(self, other_matrix):
        if self.get_rows() != other_matrix.get_rows() or self.get_columns() != other_matrix.get_columns():
            raise ValueError('Матрицы должны иметь одинаковые размеры.')
        result_matrix = []
        for i in range(self.get_rows()):
            result_row = []
            for j in range(self.get_columns()):
                result_row.append(self.matrix[i][j] + other_matrix.matrix[i][j])
            result_matrix.append(result_row)
        return Matrix(result_matrix)

    def __str__(self):
        return str(
            '\n'.join([
                str('\t'.join([
                    str(self.matrix[a][b]) for b in
                    range(len(self.matrix[a]))
                ])) for a in range(len(self.matrix))
            ])
        )


# create two matrices
matrix_a = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 5]])
matrix_b = Matrix([[5, 6, 1], [7, 8, 2], [9, 10, 11]])

# add the matrices together
result = matrix_a + matrix_b

# print the result
print(result)

