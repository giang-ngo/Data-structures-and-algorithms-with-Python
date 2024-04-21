# Bài toán quân mã đi tuần: cho bàn cờ kích thước N*N với quân mã được đặt tại vị trí ô đầu tiên.
# Di chuyển quân mã trên bàn cờ sao cho nó đi qua hết tất cả các ô của bàn cờ và mỗi ô chỉ được đi qua đúng 1 lần.
# In ra bàn cờ với thứ tự mà quân mã đã di chuyển qua từng ô.

N = 8


# kiểm tra xem việc di chuyển quan mã tới vị trí [x, y] có ok không
def is_safe(x: int, y: int, board: list) -> bool:
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


# thực hiện di chuyển con mã trên bàn cờ
def solve_knight_tour(x: int, y: int, move_step: int, board: list, x_move: list, y_move: list) -> bool:
    next_x = 0
    next_y = 0
    if move_step == N * N:  # nếu đã đi hết các bước
        return True  # có lời giải
    for i in range(N):
        next_x = x + x_move[i]  # vị trí x kế tiếp
        next_y = y + y_move[i]  # vị trí y kế tiếp
        if is_safe(next_x, next_y, board):  # nếu việc di chuyển là ok
            board[next_x][next_y] = move_step  # gán giá trị bước đi cho vị trí kế tiếp
            if solve_knight_tour(next_x, next_y, move_step + 1, board, x_move, y_move):
                return True  # báo có lời giải
            else:  # không có lời giải thì
                board[next_x][next_y] = -1  # quay lui
    return False  # không có lời giải


# hiển thị kết quả tìm được
def show_result(board: list):
    for i in range(N):
        for j in range(N):
            print(f'{board[i][j]:3}', end='')
        print()


if __name__ == '__main__':
    # tạo mảng hai chiều có NxN phần tử với giá trị khởi tạo bằng -1
    board = [[-1 for x in range(N)] for y in range(N)]
    # các cặp tọa độ mà quân mã có thể di chuyển từ vị trí hiện tại.
    x_move = [2, 1, -1, 2, -2, 1, -1, -2]
    y_move = [1, -2, 2, -1, -1, 2, -2, 1]
    # giả sử quân mã bắt đầu từ ô đầu tiên tọa độ (0, 0)
    board[0][0] = 0
    # tìm lời giải:
    result = solve_knight_tour(0, 0, 1, board, x_move, y_move)
    if result:
        print('==> Một lời giải tìm được: ')
        show_result(board)
    else:
        print('==> Không tìm thấy lời giải.')