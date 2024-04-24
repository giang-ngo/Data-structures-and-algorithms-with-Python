# *** Shell Sort

# thuật toán sắp xếp shell
def shell_sort(arr: list):
    n = len(arr)
    interval = 1  # khoảng cách giữa 2 phần tử trong mảng
    while interval < int(n / 3):  # tìm khoảng cách max
        interval = interval * 3 + 1
    while interval > 0:
        for outer in range(interval, n):
            target = arr[outer]  # phần tử đang xét
            inner = outer
            while inner > interval - 1 and arr[inner - interval] >= target:
                arr[inner] = arr[inner - interval]  # tráo đổi phần tử
                inner = inner - interval  # nhảy sang vị trí mới
            arr[inner] = target  # cập nhật phần tử tại vị trí đầu bên trái
        interval = int((interval - 1) / 3)  # cập nhật khoảng cách


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
    shell_sort(arr)
    print('==> Sau khi sắp xếp tăng dần: ')
    show_result(arr)


# hàm main
if __name__ == '__main__':
    test()
