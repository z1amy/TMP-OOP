class Matrix:
    def __init__(self, size_of_matrix):
        self.type_of_matrix = 'Matrix'
        self.size_of_matrix = size_of_matrix
        self.matrix_data = None

    def __str__(self):
        return f'\tType of Matrix = {self.type_of_matrix}\n' \
               f'\tSize of Matrix = {self.size_of_matrix}\n' \
               f'\tMatrix Data = {self.matrix_data}\n' \
               f'\tSum of all Elements = {self.sum_of_all_matrix_elements()}\n'

    def sum_of_all_matrix_elements(self):
        all_sum = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                all_sum += self.matrix_data[i][j]
        return all_sum

    def compare(self, other):
        return self.sum_of_all_matrix_elements() < other.sum_of_all_matrix_elements()

    def get_type_of_matrix(self):
        return self.type_of_matrix


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


class LowerTriangularMatrix(Matrix):
    def __init__(self, size_of_matrix):
        super().__init__(size_of_matrix)
        self.type_of_matrix = 'Lower Triangular Matrix'

    def fill_matrix(self, matrix_data):
        numbers = str.split(matrix_data, ' ')
        tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
        k = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                if i >= j:
                    tmp_matrix[i][j] = int(numbers[k])
                    k += 1
        self.matrix_data = tmp_matrix
