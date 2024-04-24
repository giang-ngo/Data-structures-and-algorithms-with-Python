import numpy as np

if __name__ == '__main__':
    arr = np.array([1, 2, 5, 4, 3, 0, 6, 9, 7, 5, 4, 2, 0])
    print('==> Mảng trước khi sắp xếp: ')
    print(arr)
    arr.sort()
    print('==> Mảng sau khi sắp xếp tăng: ')
    print(arr)

    arr[::-1].sort()  # sắp xếp giảm dần
    print('==> Mảng sau khi sắp xếp giảm: ')
    print(arr)