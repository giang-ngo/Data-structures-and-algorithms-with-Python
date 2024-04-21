# thuật toán sinh hoán vị kế tiếp
def next_permutation(arr: list) -> bool:
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] > arr[i + 1]:
        i -= 1
    if i >= 0:
        k = n - 1
        while arr[i] > arr[k]:
            k -= 1
        tmp = arr[i]
        arr[i] = arr[k]
        arr[k] = tmp
        r = i + 1
        s = n - 1
        while r < s:
            t = arr[r]
            arr[r] = arr[s]
            arr[s] = t
            r += 1
            s -= 1
        return False
    else:
        return True


# thuật toán sinh hoán vị chính tắc
def generate_permutation(arr: list):
    is_final_config = False
    while is_final_config is False:
        output(arr)
        is_final_config = next_permutation(arr)


# hàm hiển thị các phần tử trong mảng
def output(arr: list):
    for element in arr:
        print(f'{element} ', end='')
    print()  # in xuống dòng


# hàm cung cấp bộ test input đầu vào và tạo kết quả đầu ra
def test():
    n = int(input('Nhập số nguyên dương n: '))
    if n > 0:
        data = [0] * n
        # khởi tạo cấu hình đầu tiên
        for i in range(n):
            data[i] = i + 1
        # sinh các cấu hình tiếp theo
        generate_permutation(data)
    else:
        print('==> Vui lòng nhập số nguyên n > 0.')


# hàm main gọi test để chạy xem kết quả
if __name__ == '__main__':
    test()