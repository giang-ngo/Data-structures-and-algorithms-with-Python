def find_max(arr: list) -> float:
    """Hàm tìm giá trị lớn nhất trong list."""
    return max(arr)


def bucket_sort(arr: list, k: int):
    """Hàm sắp xếp bucket sort."""
    n = len(arr)
    if k < 0:
        print('==> Giá trị vùng chứa không hợp lệ.')
        return

    max_value = find_max(arr)
    buckets = [[] for _ in range(k)]

    # Phân bổ các phần tử vào vùng chứa phù hợp
    for value in arr:
        bucket_index = int((value * k) / (max_value + 1))  # max_value + 1 để tránh chỉ số vượt quá
        buckets[bucket_index].append(value)

    # Sắp xếp các vùng chứa không rỗng
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    # Gộp các phần tử lại mảng gốc
    for i, value in enumerate(sorted_arr):
        arr[i] = value


def show_data(arr: list):
    """Hàm hiển thị list kết quả trước và sau khi sắp xếp."""
    for i, value in enumerate(arr):
        print(f'{value:.2f} ', end='')
        if (i + 1) % 10 == 0:
            print()
    print()


if __name__ == '__main__':
    data = [
        8.37, 5.25, 1.25, 3.15, 0.17, 6.89, 7.54, 4.31, 3.16,
        5.78, 8.37, 0.78, 0.98, 1.48, 2.65, 3.75, 5.18, 6.24
    ]
    k = len(data)

    print('==> Trước khi sắp xếp: ')
    show_data(data)

    bucket_sort(data, k)

    print('==> Sau khi sắp xếp: ')
    show_data(data)
