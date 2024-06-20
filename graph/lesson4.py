import sys

class Edge:
    def __init__(self, start=0, end=0, weight=0):
        self.start = start
        self.end = end
        self.weight = weight

def add_edge(edges, start, end, weight):
    ''' Hàm thêm cạnh và trọng số của nó vào danh sách cạnh. '''
    edges.append(Edge(start - 1, end - 1, weight))

def bellman_ford(edges, prev, dist, size, source):
    ''' Hàm triển khai thuật toán Bellman-Ford. '''
    dist[source] = 0
    for _ in range(size - 1):
        for edge in edges:
            if dist[edge.start] != sys.maxsize and dist[edge.start] + edge.weight < dist[edge.end]:
                dist[edge.end] = dist[edge.start] + edge.weight
                prev[edge.end] = edge.start

    # kiểm tra xem đồ thị có chu trình âm không
    for edge in edges:
        if dist[edge.start] != sys.maxsize and dist[edge.start] + edge.weight < dist[edge.end]:
            print('==> Đồ thị có chu trình âm.')
            return False
    return True

def show_path(path, target):
    ''' Hàm hiển thị danh sách đỉnh trên đường đi tới đỉnh đích target. '''
    stack = []
    while target != -1:
        stack.append(target + 1)
        target = path[target]
    print(' <- '.join(map(str, reversed(stack))))

def test():
    number_vertex = int(input('Nhập số lượng đỉnh: '))
    if number_vertex > 0:
        path = [-1] * number_vertex  # danh sách đỉnh trên đường đến đỉnh đích
        dist = [sys.maxsize] * number_vertex  # danh sách khoảng cách
        edges = []  # danh sách các cạnh

        # nhập thông tin về các cạnh của đồ thị
        while True:
            args = input('Nhập đỉnh đầu, cuối, trọng số.\nNhập -1 để kết thúc: ').split()
            if len(args) < 3 or int(args[0]) == -1:
                break
            start, end, weight = map(int, args)
            add_edge(edges, start, end, weight)

        print('==================================')
        target = number_vertex - 1
        if bellman_ford(edges, path, dist, number_vertex, 0):
            print(f'==> Đường đi ngắn nhất từ đỉnh 1 -> {number_vertex}: ')
            show_path(path, target)
            print(f'Trọng số: {dist[target]}')
        else:
            print(f'==> Không có đường đi ngắn nhất từ đỉnh 1 -> {number_vertex}')
    else:
        print('==> Số lượng đỉnh phải lớn hơn 0.')

if __name__ == '__main__':
    test()
