class Vertex:
    """ Lớp mô tả thông tin về một đỉnh gồm nhãn và trạng thái ghé thăm. """
    def __init__(self, label):
        self.label = label
        self.visited = False

def dfs_recursive(vertices, adj_matrix, index):
    vertices[index].visited = True
    print(f'{vertices[index].label} ', end='')
    for i, is_connected in enumerate(adj_matrix[index]):
        if is_connected and not vertices[i].visited:
            dfs_recursive(vertices, adj_matrix, i)

def dfs_iterative(vertices, adj_matrix, index):
    stack = [index]
    while stack:
        current = stack.pop()
        if not vertices[current].visited:
            vertices[current].visited = True
            print(f'{vertices[current].label} ', end='')
            for i, is_connected in enumerate(adj_matrix[current]):
                if is_connected and not vertices[i].visited:
                    stack.append(i)

def add_vertex(vertices, label, index):
    vertices[index] = Vertex(label)

def add_edge(adj_matrix, start, end):
    adj_matrix[start][end] = True
    adj_matrix[end][start] = True

def reset_vertices(vertices):
    for vertex in vertices:
        vertex.visited = False

if __name__ == '__main__':
    num_of_vertices = int(input('Nhập số đỉnh: '))
    vertices = [None] * num_of_vertices

    for i in range(num_of_vertices):
        label = input('Tên đỉnh: ')
        add_vertex(vertices, label, i)

    adj_matrix = [[False] * num_of_vertices for _ in range(num_of_vertices)]

    while True:
        input_str = input('Nhập đỉnh đầu và đỉnh cuối (bắt đầu từ 1). Nhập -1 để kết thúc: ')
        if input_str == '-1':
            break
        start, end = map(int, input_str.split())
        add_edge(adj_matrix, start - 1, end - 1)

    print('===============================')
    dfs_iterative(vertices, adj_matrix, 0)

    reset_vertices(vertices)
    print('\n===============================')
    dfs_recursive(vertices, adj_matrix, 0)
