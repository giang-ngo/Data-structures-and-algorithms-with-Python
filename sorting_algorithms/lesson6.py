# *** Quick Sort

# thuật toán quicksort
def quicksort(arr: list, left_index: int, right_index: int):
    if left_index < right_index:
        p = partition(arr, left_index, right_index)
        quicksort(arr, left_index, p - 1)
        quicksort(arr, p + 1, right_index)


# thuật toán phân mảnh và sắp xếp các phần tử
def partition(arr: list, left: int, right: int):
    pivot = arr[right]  # phần tử chọn làm mốc
    i = left  # bắt đầu từ biên trái
    for j in range(left, right + 1):
        if arr[j] < pivot:  # phần tử tại vị trí j nhỏ hơn mốc
            arr[i], arr[j] = arr[j], arr[i]  # tráo đổi vị trí hai phần tử
            i += 1  # tăng i
    # tráo đổi phần tử tại vị trí i và right
    arr[i], arr[right] = arr[right], arr[i]
    return i  # trả về vị trí phần tử mốc kế tiếp


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
    quicksort(arr, 0, len(arr) - 1)
    print('==> Sau khi sắp xếp tăng dần bằng thuật toán quick sort: ')
    show_result(arr)


# hàm main
if __name__ == '__main__':
    test()
