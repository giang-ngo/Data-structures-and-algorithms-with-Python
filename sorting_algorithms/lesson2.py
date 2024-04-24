# *** Selection Sort

# hàm sắp xếp chọn tăng dần
def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # tiến hành tráo đổi vị trí hai phần tử
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp


# hàm hiển thị các phần tử trong mảng
def show_result(arr: list):
    for element in arr:
        print(f'{element} ', end='')
    print('\n===================================')


if __name__ == '__main__':
    # data = [int(x) for x in input('Nhập các phần tử của mảng: ').split(' ')] # mảng là các số nguyên
    data = [x for x in input('Nhập các phần tử của mảng: ').split(' ')]  # mảng là str
    print('==> Trước khi sắp xếp: ')
    show_result(data)
    print('==> Sau khi sắp xếp: ')
    selection_sort(data)
    show_result(data)
