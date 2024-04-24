# phần nâng cao của đệ quy
# Ví dụ 1: Tìm số Fibonacci Fn.
#  hàm tìm số fibonacci fn theo hướng top-down
def fibonacci_top_down(fibo: list, n: int):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    elif fibo[n] == 0:
        fibo[n] = fibonacci_top_down(fibo, n - 1) + fibonacci_top_down(fibo, n - 2)
    return fibo[n]


#  hàm tìm số fibonacci fn theo hướng bottom-up
def fibonacci_bottom_up(n: int):
    if n < 2:
        return n
    else:
        f0 = 0
        f1 = 1
        fn = 0
        for i in range(2, n + 1, 1):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return fn


if __name__ == '__main__':
    args = [0, 1, 2, 3, 10, 20, 30, 50, 90]
    print('==> Bottom-up result: ')
    for item in args:
        print(f'F{item} = {fibonacci_bottom_up(item)}')

    # solve problem with top-down strategy
    MAX_SIZE = 91
    data = [0] * MAX_SIZE
    print('==> Top-down result: ')
    for item in args:
        print(f'F{item} = {fibonacci_top_down(data, item)}')