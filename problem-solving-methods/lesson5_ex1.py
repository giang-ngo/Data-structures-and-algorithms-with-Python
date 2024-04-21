# Bài toán N quân hậu: đặt N quân hậu trên bàn cờ NxN ô sao cho các quân hậu không ăn được nhau.
N = 8

# kiểm tra xem liệu rằng đặt hậu tại vị trí [row, col]
# trên bàn cờ có ok không
def is_safe(board: list, row: int, col: int) -> bool:
    #  nếu phía trái hàng hiện thời đã có quân hậu
    for i in range(col):
        if board[row][i] == 1:
            return False  # không thể đặt quân hậu tại vị trí này
    #  kiểm tra đường chéo trên của ô hiện tại xem đã có quân hậu nào chưa
    j = col
    for i in range(row, -1, -1):
        if board[i][j] == 1:
            return False  # không thể đặt quân hậu tại vị trí này
        j -= 1
    #  kiểm tra đường chéo dưới của ô hiện tại đã có quân hậu nào chưa
    j = col
    for i in range(row, N):
        if board[i][j] == 1:
            return False  # không thể đặt quân hậu tại vị trí này
        j -= 1
    return True  # đặt được hậu tại vị trí hàng cột đang xét


# tìm lời giải
def solve_n_queen(board: list, col: int) -> bool:
    if col >= N:  # nếu đã đặt hết hậu
        return True  # báo có 1 lời giải
    # xét từng cột trên bàn cờ, đặt hậu vào hàng phù hợp
    for i in range(N):
        if is_safe(board, i, col):  # nếu tại vị trí (i, col) đặt được hậu
            board[i][col] = 1  # đặt hậu tại vịt trí này
            # nếu việc đặt hậu ở cột kế tiếp dẫn tới lời giải
            if solve_n_queen(board, col + 1):
                return True  # thông báo có lời giải
            else:  # nếu không dẫn tới lời giải
                board[i][col] = 0  # quay lui
    return False  # không có lời giải


# hiển thị kết quả tìm được
def show_result(board: list):
    for i in range(N):
        for j in range(N):
            print(f'{board[i][j]} ', end='')
        print()


if __name__ == '__main__':
    # tạo mảng hai chiều có NxN phần tử với giá trị khởi tạo bằng 0
    board = [[0 for x in range(N)] for y in range(N)]
    result = solve_n_queen(board, 0)  # tìm lời giải
    if result:  # nếu có lời giải
        print('==> Một trong các lời giải là: ')
        show_result(board)  # hiển thị lời giải lên màn hình
    else:  # nếu không có lời giải, thông báo ra màn hình
        print('==> Không tìm thấy lời giải nào')