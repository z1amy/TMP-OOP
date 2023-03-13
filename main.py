import sys
from container import CircularLinkedList


def main():
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = 'in.txt'
        output_file = 'out.txt'

    cl = CircularLinkedList()

    with open(input_file, 'r') as in_file:
        cl.read_from_file(in_file)

    cl.sort()

    with open(output_file, 'w') as out_file:
        cl.filtered_write_to_file(out_file)

    with open(output_file, 'a') as out_file:
        cl.clear()
        cl.filtered_write_to_file(out_file)


if __name__ == '__main__':
    main()
