import sys
import heapq


def has_unvisited(unvisited: list) -> bool:
    ''' Hàm kiểm tra xem còn đỉnh chưa duyệt trong danh sách đỉnh cần duyệt không. '''
    return any(unvisited)


def min_weight_vertex(dist, unvisited):
    ''' Hàm tìm chỉ số đỉnh chưa xét có trọng số nhỏ nhất '''
    min_weight = sys.maxsize
    min_vertex_index = -1
    for index in range(len(unvisited)):
        if unvisited[index] and dist[index] < min_weight:
            min_weight = dist[index]
            min_vertex_index = index
    return min_vertex_index


def dijkstra(weight_matrix, prev, size, source, target) -> int:
    ''' Hàm triển khai thuật toán Dijkstra '''
    dist = [sys.maxsize] * size  # Tạo list chứa các giá trị trọng số
    dist[source] = 0
    unvisited = [True] * size  # Tạo list chứa các đỉnh chưa được thăm
    pq = [(0, source)]  # Hàng đợi ưu tiên để quản lý các đỉnh cần xét

    while pq:
        current_dist, u = heapq.heappop(pq)

        if not unvisited[u]:
            continue

        unvisited[u] = False

        if u == target:
            return dist[u]

        for v in range(size):
            weight = weight_matrix[u][v]
            if weight != 0 and unvisited[v]:
                alt = dist[u] + weight
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(pq, (alt, v))

    return -1


def show_path(path, target):
    ''' Hàm hiển thị kết quả đường đi từ s đến e. '''
    print(1 + target, end='')
    prev_vertex = path[target]
    while prev_vertex != -1:
        print(f' <- {1 + prev_vertex}', end='')
        prev_vertex = path[prev_vertex]


def test():
    num_vertex = int(input('Nhập số đỉnh: '))
    path = [-1] * num_vertex  # Mảng lưu đường đi
    # Mảng lưu trọng số của các cạnh (u, v)
    adj_matrix = [[0 for x in range(num_vertex)] for y in range(num_vertex)]
    print('==> Nhập các cạnh: ')
    while True:
        print('Đỉnh đầu, cuối, trọng số.\nNhập -1 để kết thúc.')
        args = input().split()
        if len(args) == 1 and int(args[0]) == -1:
            break
        # Tách lấy các giá trị đỉnh đầu, cuối, trọng số
        start = int(args[0])
        end = int(args[1])
        weight = int(args[2])
        # Cập nhật trọng số đường đi từ đỉnh u -> v
        adj_matrix[start - 1][end - 1] = weight
        adj_matrix[end - 1][start - 1] = weight  # Nếu đồ thị là vô hướng

    # Tìm đường đi
    print('=========================================')
    target = num_vertex - 1
    weight = dijkstra(adj_matrix, path, num_vertex, 0, target)
    if weight >= 0:
        print(f'==> Đường đi ngắn nhất từ đỉnh 1 -> {num_vertex}: ')
        print(f'==> Trọng số: {weight}')
        show_path(path, target)
    else:
        print(f'==> Không tồn tại đường đi giữa hai đỉnh 1 -> {num_vertex}')


if __name__ == '__main__':
    test()
