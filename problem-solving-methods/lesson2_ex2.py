import numpy as np


def show_array(matrix: np.array):
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            print(f'{matrix[i,j]} ', end='')
        print()


def test():
    m, n = map(int, input("Enter m,n: ").split(' '))
    matrix = []
    for i in range(m):
        matrix.append([int(x) for x in input().split(' ')])
    array = np.array(matrix)
    show_array(array)


if __name__ == '__main__':
    test()

    # cách 1:
    # m, n = map(int, input("Enter m,n: ").split(' '))
    # matrix = []
    # array = np.array([[int(input(f"matrix[{j}][{i}]: ")) for i in range(n)] for j in range(m)])
    # array[0][0] = 100
    # print(array)
