# *** Bubble Sort

# thuật toán sắp xếp nổi bọt tăng dần
def bubble_sort_asc(arr: list):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - 1, i, -1):
            if arr[j - 1] > arr[j]:
                # đổi chỗ hai phần tử tại vị trí j và j-1
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


# thuật toán sắp xếp nổi bọt giảm dần
def bubble_sort_desc(arr: list):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - 1, i, -1):
            if arr[j - 1] < arr[j]:
                # đổi chỗ hai phần tử tại vị trí j và j-1
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


# hàm sắp xếp nổi bọt tối ưu tăng dần
def bubble_sort_opt(arr: list):
    i = len(arr) - 1
    while i > 0:
        is_swapped = False
        for j in range(i):
            # phần tử đứng trước lớn hơn phần tử đứng sau
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
        if not is_swapped:
            break
        else:
            i -= 1


# hàm hiển thị kết quả
def show_result(arr: list):
    for i in range(len(arr)):
        print(f'{arr[i]} ', end='')
    print()


def test():
    message = 'Nhập các phần tử mảng cách nhau bằng dấu cách: '
    arr = [int(x) for x in input(message).split(' ')]
    print('==> Trước khi sắp xếp: ')
    show_result(arr)
    bubble_sort_desc(arr)
    print('==> Sau khi sắp xếp giảm dần: ')
    show_result(arr)
    bubble_sort_opt(arr)
    print('==> Sau khi sắp xếp tăng dần: ')
    show_result(arr)


if __name__ == '__main__':
    test()
