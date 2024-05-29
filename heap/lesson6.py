def sift_down(data, n, index):
    """ Hàm sàng xuống. """
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right

    if largest != index:
        data[index], data[largest] = data[largest], data[index]
        sift_down(data, n, largest)


def heap_sort(data):
    """ Hàm sắp xếp heap sort. """
    n = len(data)
    bound = (n // 2) - 1
    for i in range(bound, -1, -1):
        sift_down(data, n, i)

    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        sift_down(data, i, 0)


def test():
    # Tạo dữ liệu để test chức năng sắp xếp
    data1 = [5, 2, 3, 1, 0, 4, 6, 9, 7, 8, 15]
    data2 = ["Mai", "Lan", "Huong", "Nam", "Phong", "Thanh", "Hien", "Linh", "Khanh", "Hoang", "Anh"]
    data3 = [3.25, 6.45, 8.75, 9.50, 4.68, 1.75, 8.23, 9.41, 6.14, 5.67, 7.84]

    # Hiển thị danh sách gốc
    print('==> Danh sách gốc: ')
    print(data1)
    print(data2)
    print(data3)

    # Tiến hành sắp xếp
    heap_sort(data1)
    heap_sort(data2)
    heap_sort(data3)

    # In ra kết quả sau khi sắp xếp
    print('==> Danh sách sau sắp xếp: ')
    print(data1)
    print(data2)
    print(data3)


if __name__ == '__main__':
    test()
