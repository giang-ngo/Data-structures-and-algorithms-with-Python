# *** Counting Sort

# thuật toán sắp xếp đếm
def counting_sort(arr: list):
    n = len(arr)  # lấy kích thước mảng
    k = max(arr)  # tìm phần tử có giá trị max trong mảng
    count = [0] * (k + 1)  # tạo mảng count có k + 1 phần tử
    output = [0] * n  # mảng lưu kết quả sắp xếp
    for i in range(n):  # đếm số lần xuất hiện của phần tử
        j = arr[i]  # tại vị trí i trong mảng arr
        count[j] += 1  # tăng biến đếm tại vị trí j lên 1 đơn vị
    for i in range(1, k + 1):  # tìm tổng tiền tố cho phần tử tại vị trí i
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):  # đưa các phần tử vào đúng vị trí của nó
        j = arr[i]  # lấy phần tử tại vị trí i mảng arr
        count[j] = count[j] - 1  # giảm biến đếm của nó đi 1
        output[count[j]] = arr[i]  # gán phần tử vào đúng vị trí
    for i in range(n):  # chép các phần tử từ mảng output vào mảng gốc
        arr[i] = output[i]
    del count  # thu hồi bộ nhớ cấp phát cho mảng count
    del output  # thu hồi bộ nhớ cấp phát cho mảng output


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
    counting_sort(arr)
    print('==> Sau khi sắp xếp tăng dần: ')
    show_result(arr)


# hàm main
if __name__ == '__main__':
    test()
