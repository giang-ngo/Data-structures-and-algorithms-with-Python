# *** Merge Sort

# thuật toán sắp xếp trộn đệ quy
def merge_sort(arr: list, first: int, last: int):
    if first < last:  # nếu chỉ số first nhỏ hơn last
        middle = int((first + last) / 2)  # tìm chỉ số phần tử giữa
        merge_sort(arr, first, middle)  # đệ quy nửa trái mảng
        merge_sort(arr, middle + 1, last)  # đệ quy nửa phải mảng
        merge(arr, first, middle, last)  # trộng mảng kết quả


# thuật toán trộn hai mảng đã sắp xếp
def merge(arr: list, first: int, middle: int, last: int):
    size1 = middle - first + 1  # kích thước mảng con trái
    size2 = last - middle  # kích thước mảng con phải
    left_array = [0] * size1  # tạo mảng con trái
    right_array = [0] * size2  # tạo mảng con phải
    for i in range(size1):  # chép dữ liệu vào mảng con trái
        left_array[i] = arr[first + i]
    for j in range(size2):  # chép dữ liệu vào mảng con phải
        right_array[j] = arr[middle + j + 1]
    # các biến chạy
    i = 0
    j = 0
    k = first
    while i < size1 and j < size2:  # tiến hành trộn
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            k += 1
            i += 1
        else:
            arr[k] = right_array[j]
            k += 1
            j += 1
    while i < size1:  # chép các phần tử còn lại của mảng con trái
        arr[k] = left_array[i]
        k += 1
        i += 1
    while j < size2:  # chép các phần tử còn lại của mảng con phải
        arr[k] = right_array[j]
        k += 1
        j += 1
    del left_array
    del right_array


# hàm hiển thị kết quả
def show_result(arr: list):
    for i in range(len(arr)):
        print(f'{arr[i]} ', end='')
    print()


# hàm kiểm tra kết quả trước và sau khi sắp xếp
def test():
    message = 'Nhập các phần tử mảng cách nhau bằng dấu cách: '
    arr = [int(x) for x in input(message).split(' ')]
    print('==> Trước khi sắp xếp: ')
    show_result(arr)
    merge_sort(arr, 0, len(arr) - 1)
    print('==> Sau khi sắp xếp tăng dần bằng thuật toán merge sort: ')
    show_result(arr)


# hàm main
if __name__ == '__main__':
    test()
