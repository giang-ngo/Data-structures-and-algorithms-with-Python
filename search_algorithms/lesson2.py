# thuật toán tìm kiếm nhị phân
# arr: mảng chứa các giá trị để tìm kiếm
# left: chỉ số phần tử trái cùng của đoạn cần tìm
# right: chỉ số phần tử phải cùng của đoạn cần tìm
# x: giá trị cần tìm kiếm
def binary_search(arr: list, x: int, left: int = 0, right: int = 0):
    if left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] == x:  # tìm thấy x trong mảng
            return mid
        if arr[mid] < x:  # tìm phía bên phải arr[mid]
            return binary_search(arr, x, mid + 1, right)
        else:  # tìm phía trái arr[mid]
            return binary_search(arr, x, left, mid - 1)
    return -1  # không tìm thấy


# hàm test kết quả
def test():
    message = 'Nhập các phần tử mảng cách nhau bằng dấu cách: '
    arr = [int(x) for x in input(message).split(' ')]
    x = int(input('Nhập giá trị x cần tìm: '))
    arr.sort()  # tiến hành sắp xếp mảng tăng dần
    searched_index = binary_search(arr, x, 0, len(arr) - 1)
    if searched_index > -1:
        print(f'==> Vị trí đầu tiên tìm thấy {x} trong mảng: {searched_index}')
    else:
        print(f'==> Không tìm thấy {x} trong mảng.')


# hàm main
if __name__ == '__main__':
    test()
