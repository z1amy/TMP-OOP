class Matrix:
    def __init__(self, size_of_matrix):
        self.type_of_matrix = 'Matrix'
        self.size_of_matrix = size_of_matrix
        self.matrix_data = None

    def __str__(self):
        return f'\tType of Matrix = {self.type_of_matrix}\n' \
               f'\tSize of Matrix = {self.size_of_matrix}\n' \
               f'\tMatrix Data = {self.matrix_data}\n'


class SquareMatrix(Matrix):
    def __init__(self, size_of_matrix):
        super().__init__(size_of_matrix)
        self.type_of_matrix = 'Square Matrix'

    def fill_matrix(self, matrix_data):
        numbers = str.split(matrix_data, ' ')
        tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
        k = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                tmp_matrix[i][j] = int(numbers[k])
                k += 1
        self.matrix_data = tmp_matrix


class SquareDiagonalMatrix(Matrix):
    def __init__(self, size_of_matrix):
        super().__init__(size_of_matrix)
        self.type_of_matrix = 'Square Diagonal Matrix'

    def fill_matrix(self, matrix_data):
        numbers = str.split(matrix_data, ' ')
        tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
        k = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                if i == j:
                    tmp_matrix[i][j] = int(numbers[k])
                    k += 1
        self.matrix_data = tmp_matrix
