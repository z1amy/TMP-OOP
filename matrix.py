class Matrix:
    """
    The source class for all matrices
    """
    def __init__(self, size_of_matrix, output_type):
        """
        Constructor of the Matrix class
        :param size_of_matrix: Size of the matrix
        :param output_type: Type of matrix output for printing
        """
        self.type_of_matrix = 'Matrix'
        self.size_of_matrix = size_of_matrix
        self.matrix_data = None
        self.output_type = output_type

    def __str__(self):
        """
        The first type of matrix output for printing
        """
        return f'\tType of Matrix = {self.type_of_matrix}\n' \
               f'\tSize of Matrix = {self.size_of_matrix}\n' \
               f'\tMatrix Data = {self.matrix_data}\n' \
               f'\tSum of all Elements = {self.sum_of_all_matrix_elements()}\n'

    def sum_of_all_matrix_elements(self):
        """
        The method of the class in which the sum of all elements of the matrix is calculated
        """
        all_sum = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                all_sum += self.matrix_data[i][j]
        return all_sum

    def compare(self, other):
        """
        The method of the class in which two matrices are compared by the sum of all elements of the matrix
        :param other: other matrix
        """
        return self.sum_of_all_matrix_elements() < other.sum_of_all_matrix_elements()

    def get_type_of_matrix(self):
        """
        The method of the class which returns type of matrix
        """
        return self.type_of_matrix

    def get_output_type(self):
        """
        The method of the class which returns type of matrix output for printing
        """
        return self.output_type

    def print_matrix(self):
        """
        The second type of matrix output for printing
        """
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
        out_str += f'\tSum of all Elements = {self.sum_of_all_matrix_elements()}\n'
        return out_str


class SquareMatrix(Matrix):
    """
    Class for Square Matrix
    """
    def __init__(self, size_of_matrix, output_type):
        """
        Constructor of the Square Matrix class
        :param size_of_matrix: Size of the matrix
        :param output_type: Type of matrix output for printing
        """
        super().__init__(size_of_matrix, output_type)
        self.type_of_matrix = 'Square Matrix'

    def fill_matrix(self, matrix_data):
        """
        The method of the class for filling a Square Matrix
        :param matrix_data: Data for filling matrix
        """
        numbers = str.split(matrix_data, ' ')
        tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
        k = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                tmp_matrix[i][j] = int(numbers[k])
                k += 1
        self.matrix_data = tmp_matrix


class SquareDiagonalMatrix(Matrix):
    """
    Class for Square Diagonal Matrix
    """
    def __init__(self, size_of_matrix, output_type):
        """
        Constructor of the Square Diagonal Matrix class
        :param size_of_matrix: Size of the matrix
        :param output_type: Type of matrix output for printing
        """
        super().__init__(size_of_matrix, output_type)
        self.type_of_matrix = 'Square Diagonal Matrix'

    def fill_matrix(self, matrix_data):
        """
        The method of the class for filling a Square Diagonal Matrix
        :param matrix_data: Data for filling matrix
        """
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
    """
    Class for Lower Triangular Matrix
    """
    def __init__(self, size_of_matrix, output_type):
        """
        Constructor of the Lower Triangular Matrix class
        :param size_of_matrix: Size of the matrix
        :param output_type: Type of matrix output for printing
        """
        super().__init__(size_of_matrix, output_type)
        self.type_of_matrix = 'Lower Triangular Matrix'

    def fill_matrix(self, matrix_data):
        """
        The method of the class for filling the Lower Triangular Matrix
        :param matrix_data: Data for filling matrix
        """
        numbers = str.split(matrix_data, ' ')
        tmp_matrix = [[0 for _ in range(self.size_of_matrix)] for _ in range(self.size_of_matrix)]
        k = 0
        for i in range(self.size_of_matrix):
            for j in range(self.size_of_matrix):
                if i >= j:
                    tmp_matrix[i][j] = int(numbers[k])
                    k += 1
        self.matrix_data = tmp_matrix


def check(matrix_1, matrix_2):
    """
    The function that compares two classes of matrices
    :param matrix_1: First matrix for check
    :param matrix_2: Second matrix for check
    """
    match matrix_1, matrix_2:
        case SquareMatrix(), SquareMatrix():
            print('Matrices belong to the same type: Square Matrix')
        case SquareMatrix(), SquareDiagonalMatrix():
            print('Matrices belong to the different types: Square Matrix and Square Diagonal Matrix')
        case SquareMatrix(), LowerTriangularMatrix():
            print('Matrices belong to the different types: Square Matrix and Lower Triangular Matrix')
        case SquareDiagonalMatrix(), SquareDiagonalMatrix():
            print('Matrices belong to the same type: Square Diagonal Matrix')
        case SquareDiagonalMatrix(), SquareMatrix():
            print('Matrices belong to the different types: Square Diagonal Matrix and Square Matrix')
        case SquareDiagonalMatrix(), LowerTriangularMatrix():
            print('Matrices belong to the different types: Square Diagonal Matrix and Lower Triangular Matrix')
        case LowerTriangularMatrix(), LowerTriangularMatrix():
            print('Matrices belong to the same type: Lower Triangular Matrix')
        case LowerTriangularMatrix(), SquareMatrix():
            print('Matrices belong to the different types: Lower Triangular Matrix and Square Matrix')
        case LowerTriangularMatrix(), SquareDiagonalMatrix():
            print('Matrices belong to the different types: Lower Triangular Matrix and Square Diagonal Matrix')
        case _:
            print('Unknown type')
            return

    print(f'First: type={type(matrix_1)}, id={id(matrix_1)}\nSecond: type={type(matrix_2)}, id={id(matrix_2)}\n')
