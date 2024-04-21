def show_matrix(data: list):
    for row in data:
        for value in row:
            print(f'{value} ', end='')
        print()
    print('================================')


def show_via_index(data: list):
    for i in range(len(data)):
        # for j in range(data[i].__len__()):
        for j in range(len(data[i])):
            print(f'matrix[{i}][{j}]={data[i][j]} ', end='')
        print()


if __name__ == '__main__':
    m, n = map(int, input("Enter m,n: ").split(' '))
    matrix = [[int(input(f'matrix[{j}][{i}]: ')) for i in range(n)] for j in range(m)]
    show_matrix(matrix)

    # matrix = []
    # for i in range(m):
    #     row = [int(x) for x in input().split(' ')]
    #     matrix.append(row)
    #
    # show_matrix(matrix)

    # k = 50
    # m = 4  # số cột
    # n = 5  # số hàng
    # matrix = [[k for x in range(m)] for y in range(n)]
    # show_matrix(matrix)
    # matrix[0][1] = 8
    # matrix[1][2] = 6
    # matrix[2][3] = 6
    # matrix[4][3] = 9
    # show_matrix(matrix)
    # show_via_index(matrix)
