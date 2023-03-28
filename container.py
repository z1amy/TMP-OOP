from matrix import SquareMatrix, SquareDiagonalMatrix, LowerTriangularMatrix, check
import sys


class Node:
    """
    Class describing the node of Circular Linked List
    """
    def __init__(self, data):
        """
        Constructor of the Node class
        :param data: The data contained in the class (matrix)
        """
        self.data = data
        self.next = None


class CircularLinkedList:
    """
    Class representing the implementation of the container (Circular Linked List)
    """
    def __init__(self):
        """
        Constructor of the Circular Linked List class
        """
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        """
        The method of the class which returns the length of the container
        """
        return self.size

    def clear(self):
        """
        The method of the class in which the container is being cleaned
        """
        self.__init__()

    def add(self, data):
        """
        The method of the class in which new node adds to the container
        :param data: The data contained in the new node
        """
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
        """
        The method of the class in which the file is read and the container is filled
        :param in_file: Input file
        """
        for line in in_file:
            data = line.strip().split(';')
            try:
                type_of_matrix = int(data[0].strip())
                size_of_matrix = int(data[1].strip())
                output_type = int(data[2].strip())
            except ValueError:
                print(f'Invalid input data format!\n'
                      f'Line: {line}\n')
                continue
            matrix_data = data[3].strip()
            if type_of_matrix == 1:
                new_matrix = SquareMatrix(size_of_matrix, output_type)
                try:
                    new_matrix.fill_matrix(matrix_data)
                except (IndexError, ValueError):
                    print(f'Invalid input data format!\n'
                          f'Line: {line}\n')
                    continue
            elif type_of_matrix == 2:
                new_matrix = SquareDiagonalMatrix(size_of_matrix, output_type)
                try:
                    new_matrix.fill_matrix(matrix_data)
                except (IndexError, ValueError):
                    print(f'Invalid input data format!\n'
                          f'Line: {line}\n')
                    continue
            elif type_of_matrix == 3:
                new_matrix = LowerTriangularMatrix(size_of_matrix, output_type)
                try:
                    new_matrix.fill_matrix(matrix_data)
                except (IndexError, ValueError):
                    print(f'Invalid input data format!\n'
                          f'Line: {line}\n')
                    continue
            else:
                continue
            self.add(new_matrix)

    def write_to_file(self, out_file):
        """
        The method of the class in which the container is written to the file
        :param out_file: Output file
        """
        current = self.head
        try:
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
        except OSError:
            print(f'File writing error {out_file}!')
            sys.exit(1)

    def filtered_write_to_file(self, out_file):
        """
        The method of the class in which the filtered container is written to the file
        Only square matrices are written
        :param out_file: Output file
        """
        current = self.head
        try:
            if self.head is None:
                out_file.write('Container is empty!\n')
            else:
                i = 0
                out_file.write('Filled Container:\n')
                if current.data.get_type_of_matrix() == 'Square Matrix':
                    if current.data.get_output_type() == 1:
                        out_file.write(f'{i}: {str(current.data.print_matrix())}')
                    else:
                        out_file.write(f'{i}: {str(current.data)}')
                while current.next != self.head:
                    i += 1
                    current = current.next
                    if current.data.get_type_of_matrix() == 'Square Matrix':
                        if current.data.get_output_type() == 1:
                            out_file.write(f'{i}: {str(current.data.print_matrix())}')
                        else:
                            out_file.write(f'{i}: {str(current.data)}')
            out_file.write(f'Container contains {self.__len__()} elements.\n')
        except OSError:
            print(f'File writing error {out_file}!')
            sys.exit(1)

    def sort(self):
        """
        The method of the class in which the container is sorted
        """
        if self.head is not None:
            node1 = self.head
            node2 = self.head.next
            while True:
                while True:
                    if node1.data.compare(node2.data):
                        node1.data, node2.data = node2.data, node1.data
                    node2 = node2.next
                    if node2 is self.head:
                        break
                node1 = node1.next
                node2 = self.head
                if node1 is self.head:
                    break

    def check_matrices(self):
        """
        The method of the class in which container nodes are compared
        """
        node1 = self.head
        while True:
            node2 = self.head
            while True:
                check(node1.data, node2.data)
                node2 = node2.next
                if node2 == self.head:
                    break
            node1 = node1.next
            if node1 == self.head:
                break
