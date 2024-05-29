# lớp mô tả thông tin một node
class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


# lớp mô tả stack và các hành động
class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0

    # phương thức thêm node vào đầu stack
    def push(self, data):
        p = Node(data)  # tạo mới một node với dữ liệu cho trước
        self.__size += 1
        if self.is_empty():  # nếu danh sách rỗng
            self.__head = p
        else:  # nếu danh sách không rỗng
            p.next = self.__head
            self.__head = p

    # phương thức xóa node đầu stack
    def pop(self):
        if self.__size == 0:
            print('Stack is empty')
            return None
        else:
            value = self.__head.data
            self.__head = self.__head.next
            self.__size -= 1
            return value

    # phương thức dùng để kiểm tra DSLK có rỗng không
    def is_empty(self):
        return self.__size == 0

    # phương thức trả về phần tử top
    def top(self):
        if self.is_empty():
            print('==> Stack rỗng')
            return None
        else:
            return self.__head.data

    # phương thức trả về số phần tử hiện có trong stack
    def size(self):
        return self.__size

    # phương thức dùng để hiển thị các phần tử trong DSLK
    def show_elements(self):
        p = self.__head  # xuất phát từ node đầu tiên trong DSLK
        while p is not None:  # lặp chừng nào chưa hết danh sách
            print(f'{p.data} -> ', end='')  # in ra giá trị của node đang xét
            p = p.next  # chuyển sang node kế tiếp
        print('None')  # cuối cùng khi đã in xong in ra None => kết thúc DSLK


if __name__ == '__main__':
    stack = Stack()
    # thêm các node vào đầu DSLK
    stack.push("Mai")
    stack.push("Loan")
    stack.push("Khoa")
    stack.push("Linh")
    stack.push("Long")
    stack.push("Trang")
    stack.push("Vy")
    print('==> Stack sau khi thêm các node vào stack: ')
    stack.show_elements()
    print(f'==> Số lượng phần tử trong stack: {stack.size()}')
    print(f'==> Phần tử top: {stack.top()}')

    # xóa phần tử top
    stack.pop()
    print('SAU KHI XÓA PHẦN TỬ TOP: ')
    print(f'==> Số lượng phần tử trong stack: {stack.size()}')
    print(f'==> Phần tử top: {stack.top()}')

    # hiển thị các phần tử còn lại của stack
    print('==> Các phần tử của stack: ')
    stack.show_elements()
