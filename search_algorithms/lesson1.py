# thuật toán tìm kiếm tuyến tính
def linear_search(arr: list, x: int) -> int:
    for i in range(len(arr)):  # xuất phát từ đầu mảng
        if arr[i] == x:  # nếu tìm thấy x trong mảng
            return i  # trả về vị trí đầu tiên xuất hiện x
    return -1  # không tìm thấy


# hàm hiển thị kết quả
def show_result(arr: list):
    for i in range(len(arr)):
        print(f'{arr[i]} ', end='')
    print()


# hàm test kết quả
def test():
    message = 'Nhập các phần tử mảng cách nhau bằng dấu cách: '
    arr = [int(x) for x in input(message).split(' ')]
    x = int(input('Nhập giá trị x cần tìm: '))
    searched_index = linear_search(arr, x)
    if searched_index > -1:
        print(f'==> Vị trí đầu tiên tìm thấy {x} trong mảng: {searched_index}')
    else:
        print(f'==> Không tìm thấy {x} trong mảng.')


# hàm main
if __name__ == '__main__':
    test()