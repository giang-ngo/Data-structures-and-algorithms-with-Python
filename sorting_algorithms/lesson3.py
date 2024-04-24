# *** Insertion Sort

# thuật toán sắp xếp chèn tăng dần
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        target = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = target


# hàm hiển thị kết quả
def show_result(arr: list):
    for i in range(len(arr)):
        print(f'{arr[i]} ', end='')
    print()


# hàm test kết quả
def test():
    message = 'Nhập các phần tử mảng cách nhau bằng dấu cách: '
    arr = [int(x) for x in input(message).split(' ')]
    print('==> Trước khi sắp xếp: ')
    show_result(arr)
    insertion_sort(arr)
    print('==> Sau khi sắp xếp tăng dần: ')
    show_result(arr)


# hàm main
if __name__ == '__main__':
    test()
