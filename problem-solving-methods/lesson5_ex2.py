# bài toán Knight's Tour
N = 8

# kiểm tra xem việc di chuyển quân mã tới vị trí [x, y] có ok không
def is_safe(x: int, y: int, board: list) -> bool:
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# tìm số lượng nước đi hợp lệ từ vị trí [x, y]
def get_degree(x: int, y: int, board: list, x_move: list, y_move: list) -> int:
    count = 0
    for i in range(8):
        if is_safe(x + x_move[i], y + y_move[i], board):
            count += 1
    return count

# thực hiện di chuyển con mã trên bàn cờ
def solve_knight_tour(x: int, y: int, move_step: int, board: list, x_move: list, y_move: list) -> bool:
    if move_step == N * N:  # nếu đã đi hết các bước
        return True  # có lời giải

    # danh sách các nước đi tiếp theo cùng với số lượng nước đi hợp lệ tiếp theo
    next_moves = []
    for i in range(8):
        next_x = x + x_move[i]
        next_y = y + y_move[i]
        if is_safe(next_x, next_y, board):
            degree = get_degree(next_x, next_y, board, x_move, y_move)
            next_moves.append((degree, next_x, next_y))

    # sắp xếp các nước đi theo số lượng nước đi hợp lệ tiếp theo tăng dần
    next_moves.sort()

    for degree, next_x, next_y in next_moves:
        board[next_x][next_y] = move_step  # gán giá trị bước đi cho vị trí kế tiếp
        if solve_knight_tour(next_x, next_y, move_step + 1, board, x_move, y_move):
            return True  # báo có lời giải
        else:  # không có lời giải thì
            board[next_x][next_y] = -1  # quay lui
    return False  # không có lời giải

# hiển thị kết quả tìm được
def show_result(board: list):
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))

if __name__ == '__main__':
    # tạo mảng hai chiều có NxN phần tử với giá trị khởi tạo bằng -1
    board = [[-1 for _ in range(N)] for _ in range(N)]
    # các cặp tọa độ mà quân mã có thể di chuyển từ vị trí hiện tại.
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]
    # giả sử quân mã bắt đầu từ ô đầu tiên tọa độ (0, 0)
    board[0][0] = 0
    # tìm lời giải:
    result = solve_knight_tour(0, 0, 1, board, x_move, y_move)
    if result:
        print('==> Một lời giải tìm được: ')
        show_result(board)
    else:
        print('==> Không tìm thấy lời giải.')
