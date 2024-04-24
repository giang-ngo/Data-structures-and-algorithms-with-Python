# phần nâng cao của đệ quy
# Ví dụ 2: Cho biết có bao nhiêu cách lập nên một số n >= 0 từ tập các con số {1, 3, 5}?.
'''
###
=> tạo số 0: 1 cách là không chọn số nào cả.
###
=> tạo số 1: 1 cách là chọn 1 số 1
###
=> tạo số 2: 1 cách là cộng hai số 1
###
=> tạo số 3: 2 cách
1 + 1 + 1
3
###
=> tạo số 4: 3 cách
1 + 1 + 1 + 1
1 + 3
3 + 1
###
=> tạo số 5: 5 cách
1 + 1 + 1 + 1 + 1
1 + 1 + 3
1 + 3 + 1
3 + 1 + 1
5
Nếu chọn số 1, thì còn lại n − 1 phải tạo.
Nếu chọn số 3, thì còn lại n − 3 phải tạo.
Nếu chọn số 5, thì còn lại n − 5 phải tạo.

==> tổng số cách tạo số n = T(n - 1) + T(n - 3) + T(n - 5)
T(5) = T(5 - 1) + T(5 - 3) + T(5 - 5)
T(5) = T(4) + T(2) + T(0) = 3 + 1 + 1 = 5
'''


#  top-down strategy
def build_n_top_down(dp: list, n: int):
    if n < 0:
        dp[0] = 0
        return dp[0]
    elif n == 0:
        dp[1] = 1
        return dp[1]
    elif dp[n] == 0:
        dp[n] = (build_n_top_down(dp, n - 1)
                 + build_n_top_down(dp, n - 3)
                 + build_n_top_down(dp, n - 5))
    return dp[n]


# bottom-up strategy
def build_n_bottom_up(n: int):
    result = [0] * (n + 1)
    result[0] = 1
    for i in range(1, n + 1):
        result[i] = result[i] + result[i - 1]
        if i - 3 >= 0:
            result[i] = result[i] + result[i - 3]
        if i - 5 >= 0:
            result[i] = result[i] + result[i - 5]
    return_value = result[n]
    del result
    return return_value


if __name__ == '__main__':
    MAX_SIZE = 100
    params = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]
    print(f'==> Hướng tiếp cận top-down: ')
    for item in params:
        data = [0] * (MAX_SIZE + 1)
        print(f'Tạo số {item}: {build_n_top_down(data, item)}')
        del data

    print(f'==> Hướng tiếp cận bottom-up: ')
    for item in params:
        print(f'Tạo số {item}: {build_n_bottom_up(item)}')
