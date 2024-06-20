N = 8

# kiểm tra xem liệu rằng đặt hậu tại vị trí [row, col]
# trên bàn cờ có ok không
def is_safe(board: list, row: int, col: int) -> bool:
    # kiểm tra phía bên trái hàng hiện tại
    for i in range(col):
        if board[row][i] == 1:
            return False
    # kiểm tra đường chéo trên bên trái
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # kiểm tra đường chéo dưới bên trái
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

# tìm lời giải
def solve_n_queen(board: list, col: int) -> bool:
    if col >= N:  # nếu đã đặt hết hậu
        return True  # báo có 1 lời giải
    # xét từng hàng trên bàn cờ, đặt hậu vào cột phù hợp
    for row in range(N):
        if is_safe(board, row, col):  # nếu tại vị trí (row, col) đặt được hậu
            board[row][col] = 1  # đặt hậu tại vị trí này
            # nếu việc đặt hậu ở cột kế tiếp dẫn tới lời giải
            if solve_n_queen(board, col + 1):
                return True  # thông báo có lời giải
            # nếu không dẫn tới lời giải, quay lui
            board[row][col] = 0
    return False  # không có lời giải

# hiển thị kết quả tìm được
def show_result(board: list):
    for row in board:
        print(" ".join(str(x) for x in row))

if __name__ == '__main__':
    # tạo mảng hai chiều có NxN phần tử với giá trị khởi tạo bằng 0
    board = [[0 for _ in range(N)] for _ in range(N)]
    result = solve_n_queen(board, 0)  # tìm lời giải
    if result:  # nếu có lời giải
        print('==> Một trong các lời giải là: ')
        show_result(board)  # hiển thị lời giải lên màn hình
    else:  # nếu không có lời giải, thông báo ra màn hình
        print('==> Không tìm thấy lời giải nào')
