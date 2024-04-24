# *** Radix Sort

# thuật toán counting sort
def counting_sort(arr: list, exp: int):  # arr: mảng đầu vào
    n = len(arr)  # lấy số phần tử mảng
    k = 9  # số chữ số tối đa của giá trị kiểu int(~2.1 tỉ)
    count = [0] * (k + 1)  # tạo mảng count có k + 1 phần tử
    output = [0] * n  # tạo mảng output có n phần tử
    # đếm số lần xuất hiện của kí tự ở hàng exp(đơn vị, chục, trăm...)
    for i in range(n):
        j = int(arr[i] / exp) % 10  # lấy chữ số ở hàng exp
        count[j] += 1  # tăng biến đếm tại vị trí j lên 1
    # tính tổng tiền tố cho p.tử vị trí i
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    # đưa các phần tử vào đúng vị trí của nó
    for i in range(n - 1, -1, -1):
        j = int(arr[i] / exp) % 10  # lấy phần tử tại vị trí i của mảng arr
        count[j] -= 1  # giảm biến đếm của nó đi 1
        output[count[j]] = arr[i]  # gán phần tử vào vị trí
    # sao chép các phần tử trong mảng vào mảng gốc
    for i in range(n):
        arr[i] = output[i]


# thuật toán radix sort
def radix_sort(arr: list):
    max_value = max(arr)
    i = 1
    while int(max_value / i) > 0:
        counting_sort(arr, i)
        i *= 10


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
    radix_sort(arr)
    print('==> Sau khi sắp xếp tăng dần: ')
    show_result(arr)


# hàm main
if __name__ == '__main__':
    test()
