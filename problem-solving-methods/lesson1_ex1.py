from array import array


def count_x(arr: array, x: int) -> int:
    return arr.count(x)


if __name__ == '__main__':
    # integer_numbers = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    # integer_numbers.fromlist([9, 9, 9, 9, 9, 9, 9, 988])
    # integer_numbers.append(500)
    #
    # print(integer_numbers)
    # integer_numbers.reverse()
    # print(integer_numbers)
    # print(integer_numbers.count(9))

    input_str = input("Enter integer numbers: ")
    x = int(input('Enter x: '))
    integer_list = [int(e) for e in input_str.split(' ')]
    integer_array = array('i', integer_list)
    print(f'Number occurrence of {x}: {count_x(integer_array, x)}')
