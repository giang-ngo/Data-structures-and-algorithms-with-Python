# thuật toán sinh tổ hợp kế tiếp
def next_combination(arr: list, n: int, k: int) -> bool:  # arr: chứa cấu hình hiện tại
    i = k - 1  # xuất phát từ phần tử cuối của tổ hợp
    while i >= 0 and arr[i] == n - k + i + 1:  # tìm phần tử arr[i] đầu tiên khác n-k+i+1
        i -= 1
    if i >= 0:  # nếu i chưa vượt quá phần tử trái cùng
        arr[i] = arr[i] + 1  # thay x[i] = x[i]+1
        for j in range(i + 1, k):  # cập nhật các phần tử từ vị trí i+1 đến k
            arr[j] = arr[i] + j - i  # gán arr[j] = arr[i] + j - i
        return False  # thông báo cho nơi gọi biết đây chưa phải cấu hình cuối
    else:
        return True  # thông báo cho nơi gọi biết đây là cấu hình cuối cùng


# thuật toán sinh tổ hợp chập k của n
def generate(arr: list, n: int, k: int):
    is_final_config = False
    while not is_final_config:
        output(arr)
        is_final_config = next_combination(arr, n, k)


# hàm hiển thị các phần tử trong mảng
def output(arr: list):
    for element in arr:
        print(f'{element} ', end='')
    print()  # in xuống dòng


# hàm test kết quả
def test():
    n, k = map(int, input('Nhập số nguyên dương n, k cách nhau một dấu cách: ').split(' '))
    if n > 0 and 0 < k <= n:
        data = [0] * k
        # khởi tạo cấu hình đầu tiên
        for i in range(k):
            data[i] = i + 1
        # sinh các cấu hình tiếp theo
        print(f'==> Các tổ hợp C({k}, {n}): ')
        generate(data, n, k)
    else:
        print('==> Vui lòng nhập số nguyên n n và 0 < k <= n.')


if __name__ == '__main__':
    test()