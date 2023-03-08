from matrix import SquareMatrix, SquareDiagonalMatrix


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def clear(self):
        self.__init__()

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1

    def read_from_file(self, in_file):
        lines = in_file.readlines()
        if len(lines) % 4 != 0:
            return

        for index in range(0, len(lines), 4):
            type_of_matrix = int(lines[index].strip())
            size_of_matrix = int(lines[index + 1].strip())
            output_type = int(lines[index + 2].strip())
            matrix_data = lines[index + 3].strip()
            new_matrix = None
            if type_of_matrix == 1:
                new_matrix = SquareMatrix(size_of_matrix, output_type)
                new_matrix.fill_matrix(matrix_data)
            elif type_of_matrix == 2:
                new_matrix = SquareDiagonalMatrix(size_of_matrix, output_type)
                new_matrix.fill_matrix(matrix_data)
            self.add(new_matrix)

    def write_to_file(self, out_file):
        current = self.head
        if self.head is None:
            out_file.write('Container is empty!\n')
        else:
            i = 0
            out_file.write('Filled Container:\n')
            if current.data.get_output_type() == 1:
                out_file.write(f'{i}: {str(current.data.print_matrix())}')
            else:
                out_file.write(f'{i}: {str(current.data)}')
            while current.next != self.head:
                i += 1
                current = current.next
                if current.data.get_output_type() == 1:
                    out_file.write(f'{i}: {str(current.data.print_matrix())}')
                else:
                    out_file.write(f'{i}: {str(current.data)}')
        out_file.write(f'Container contains {self.__len__()} elements.\n')
