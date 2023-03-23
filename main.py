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

    try:
        with open(input_file, 'r') as in_file:
            cl.read_from_file(in_file)
    except OSError:
        print(f'File opening error {in_file}!')
        sys.exit(1)

    cl.sort()
    cl.check_matrices()

    try:
        with open(output_file, 'w') as out_file:
            # cl.filtered_write_to_file(out_file)
            cl.write_to_file(out_file)

        with open(output_file, 'a') as out_file:
            cl.clear()
            # cl.filtered_write_to_file(out_file)
            cl.write_to_file(out_file)
    except OSError:
        print(f'File writing error {out_file}!')
        sys.exit(1)


if __name__ == '__main__':
    main()
