class Vertex:
    """Lớp mô tả thông tin về một đỉnh gồm nhãn và trạng thái ghé thăm."""

    def __init__(self, label):
        self.label = label
        self.visited = False


def add_vertex(vertices, label, index):
    vertices[index] = Vertex(label)


def add_edge(adj_matrix, start, end):
    adj_matrix[start][end] = adj_matrix[end][start] = True


def bfs(vertices, adj_matrix, index):
    """Thuật toán duyệt theo chiều rộng."""
    queue = [index]
    vertices[index].visited = True

    while queue:
        current_index = queue.pop(0)
        print(vertices[current_index].label, end=' ')

        for neighbor_index, is_connected in enumerate(adj_matrix[current_index]):
            if is_connected and not vertices[neighbor_index].visited:
                vertices[neighbor_index].visited = True
                queue.append(neighbor_index)


def reset_vertices(vertices):
    for vertex in vertices:
        vertex.visited = False


def main():
    num_of_vertex = int(input('Nhập số đỉnh: '))
    vertices = [None] * num_of_vertex

    for i in range(num_of_vertex):
        label = input(f'Tên đỉnh {i + 1}: ')
        add_vertex(vertices, label, i)

    adj_matrix = [[False] * num_of_vertex for _ in range(num_of_vertex)]

    while True:
        input_str = input('Nhập đỉnh đầu, đỉnh cuối (bắt đầu từ 1). Nhập -1 để kết thúc: ')
        if input_str == '-1':
            break

        start, end = map(int, input_str.split())
        add_edge(adj_matrix, start - 1, end - 1)

    print('===============================')
    print('==> Kết quả duyệt đồ thị bằng thuật toán BFS: ')
    bfs(vertices, adj_matrix, 0)


if __name__ == '__main__':
    main()
