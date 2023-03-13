class Matrix:
    def __init__(self, size_of_matrix, output_type):
        self.type_of_matrix = 'Matrix'
        self.size_of_matrix = size_of_matrix
        self.matrix_data = None
        self.output_type = output_type

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

    def get_output_type(self):
        return self.output_type

    def print_matrix(self):
        out_str = f'\tType of Matrix = {self.type_of_matrix}\n' \
                  f'\tSize of Matrix = {self.size_of_matrix}\n' \
                  f'\tMatrix Data:\n'
        for i in range(self.size_of_matrix):
            out_str += f'\t'
            for j in range(self.size_of_matrix):
                if j != self.size_of_matrix - 1:
                    out_str += f'{self.matrix_data[i][j]}\t'
                else:
                    out_str += f'{self.matrix_data[i][j]}'
            out_str += f'\n'
        return out_str


class SquareMatrix(Matrix):
    def __init__(self, size_of_matrix, output_type):
        super().__init__(size_of_matrix, output_type)
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
    def __init__(self, size_of_matrix, output_type):
        super().__init__(size_of_matrix, output_type)
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
