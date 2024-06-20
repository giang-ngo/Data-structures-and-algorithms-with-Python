import sys  # Thư viện chứa giá trị max của kiểu int

class Edge:
    ''' Lớp mô tả một cạnh trong đồ thị. '''
    def __init__(self, start=0, end=0, weight=0):
        self.start = start  # Điểm đầu
        self.end = end  # Điểm cuối
        self.weight = weight  # Trọng số cạnh

def add_edge(edges, start, end, weight):
    ''' Hàm thêm cạnh và trọng số của nó vào danh sách cạnh. '''
    edge = Edge(start - 1, end - 1, weight)
    edges.append(edge)

def floyd_warshall(edges, dist, next, size):
    ''' Hàm triển khai thuật toán Floyd-Warshall. '''
    for e in edges:
        dist[e.start][e.end] = e.weight
        next[e.start][e.end] = e.end
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize:
                    alt = dist[i][k] + dist[k][j]
                    if dist[i][j] > alt:
                        dist[i][j] = alt
                        next[i][j] = next[i][k]

def min_path(next, path, u, v):
    ''' Hàm tìm đường đi ngắn nhất giữa hai đỉnh u, v. '''
    if next[u][v] == -1:
        return
    path.append(u)
    while u != v:
        u = next[u][v]
        path.append(u)

def show_path(path):
    ''' Hàm hiển thị danh sách đỉnh trên đường đi. '''
    for i in range(len(path)):
        print(f'{1 + path[i]}', end='')
        if i < len(path) - 1:
            print(' -> ', end='')
    print()

def test():
    ''' Hàm kiểm tra chương trình có chạy đúng không. '''
    number_vertex = int(input('Nhập số lượng đỉnh: '))
    if number_vertex > 0:
        path = []  # Danh sách đỉnh trên đường đến đỉnh đích
        dist = [[sys.maxsize for _ in range(number_vertex)] for _ in range(number_vertex)]
        next = [[-1 for _ in range(number_vertex)] for _ in range(number_vertex)]
        edges = []  # Danh sách các cạnh

        # Nhập thông tin về các cạnh của đồ thị
        while True:
            print('Nhập đỉnh đầu, cuối, trọng số.\nNhập -1 để kết thúc: ')
            args = input().split()
            if len(args) > 0:
                start = int(args[0])
                if start == -1:
                    break
                end = int(args[1])
                weight = int(args[2])
                add_edge(edges, start, end, weight)

        print('==================================')
        target = number_vertex - 1
        source = 0
        floyd_warshall(edges, dist, next, number_vertex)
        min_path(next, path, source, target)
        if len(path) > 0:
            print(f'==> Đường đi ngắn nhất từ đỉnh 1 -> {number_vertex}: ')
            show_path(path)
            print(f'Trọng số: {dist[source][target]}')
        else:
            print(f'==> Không có đường đi ngắn nhất từ đỉnh 1 -> {number_vertex}')
    else:
        print('==> Số lượng đỉnh phải lớn hơn 0.')

if __name__ == '__main__':
    test()
