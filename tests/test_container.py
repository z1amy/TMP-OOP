from container import CircularLinkedList


def test_clear():
    cl = CircularLinkedList()
    for i in range(10):
        cl.add(i)
    cl.clear()

    assert cl.size == 0


def test_add():
    cl = CircularLinkedList()
    for i in range(10):
        cl.add(i)

    assert cl.size == 10


def test_read_from_file():
    cl = CircularLinkedList()
    with open('in.txt', 'r') as in_file:
        cl.read_from_file(in_file)

    assert cl.size != 0


def test_write_to_file():
    cl = CircularLinkedList()
    with open('in.txt', 'r') as in_file:
        cl.read_from_file(in_file)
    with open('write.txt', 'w') as out_file:
        cl.write_to_file(out_file)

    with open('write.txt', 'r') as write, open('test_write.txt', 'r') as test_write:
        assert write.read() == test_write.read()


def test_filtered_write_to_file():
    cl = CircularLinkedList()
    with open('in.txt', 'r') as in_file:
        cl.read_from_file(in_file)
    with open('filtered_write.txt', 'w') as out_file:
        cl.filtered_write_to_file(out_file)

    with open('filtered_write.txt', 'r') as filtered_write, open('test_filtered_write.txt', 'r') as test_filtered_write:
        assert filtered_write.read() == test_filtered_write.read()


def test_sort():
    cl = CircularLinkedList()
    with open('in.txt', 'r') as in_file:
        cl.read_from_file(in_file)
    cl.sort()
    with open('sort.txt', 'w') as out_file:
        cl.write_to_file(out_file)

    with open('sort.txt', 'r') as sort, open('test_sort.txt', 'r') as test_sort:
        assert sort.read() == test_sort.read()
