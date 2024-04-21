# hàm in ra chuỗi kết quả
def print_result(result: list):
    for item in result:
        print(f'{item} ', end='')
    print()


# hàm sinh cấu hình kế tiếp
def next_configuration(result: list, n: int) -> bool:
    i = n - 1
    while i >= 0 and result[i] != 0:
        result[i] = 0
        i -= 1
    if i >= 0:
        result[i] = 1
        return False  # đánh dấu chưa phải cấu hình cuối cùng
    else:
        return True  # đánh dấu đây là cấu hình cuối cùng


# hàm quản lý việc sinh sâu nhị phân và in ra kết quả
def generate_binary_string(result: list, n: int):
    is_final_config = False
    while is_final_config is False:
        print_result(result)
        is_final_config = next_configuration(result, n)


if __name__ == '__main__':
    size = int(input('Nhập số nguyên dương n: '))
    if size > 0:
        arr = [0] * size
        generate_binary_string(arr, size)
    else:
        print('Vui lòng nhập số nguyên n > 0.')