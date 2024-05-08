from stack.student import Student


# lớp mô tả một stack và các hành động của nó
class Stack:
    def __init__(self, capacity=0):
        self.__data: list = []
        self.__capacity: int
        self.__size: int = 0
        # giả định rằng capacity khi không chỉ định là 10
        if capacity <= 0:
            self.__capacity = 10
        else:
            self.__capacity = capacity

    # phương thức kiểm tra stack rỗng
    def is_empty(self):
        return self.__size == 0

    # phương thức thêm mới phần tử vào stack
    def push(self, value) -> bool:
        if self.is_full():
            print('==> Stack đầy. Thêm thất bại.')
            return False
        else:
            self.__data.append(value)
            self.__size += 1
            return True

    # phương thức xóa bỏ phần tử cuối
    def pop(self):
        if self.is_empty():
            print('==> Stack rỗng')
            return None
        else:
            element = self.__data.pop()
            self.__size -= 1
            return element

    # phương thức lấy ra phần tử top
    def top(self):
        if self.is_empty():
            print('==> Stack rỗng')
            return None
        else:
            element = self.__data[self.__size - 1]
            return element

    # phương thức trả về kích thước hiện thời
    def size(self):
        return self.__size

    # phương thức kiểm tra stack đã đầy chưa
    def is_full(self):
        return self.__size == self.__capacity


# hàm hiển thị các phần tử trong stack
def show_stack_elements(stack: Stack):
    while not stack.is_empty():
        print(stack.pop())


# hàm test các chức năng
def test():
    students = [
        Student("SV1001", "Nam", "Hoàng", 3.26),
        Student("SV1002", "Hoa", "Lương", 3.36),
        Student("SV1003", "Bách", "Ngô", 3.21),
        Student("SV1004", "Trung", "Trần", 3.54),
        Student("SV1005", "Loan", "Lê", 3.04),
        Student("SV1006", "Mai", "Nguyễn", 3.87),
        Student("SV1007", "Khoa", "Lê", 3.71),
        Student("SV1008", "Ánh", "Nguyễn", 3.64),
        Student("SV1009", "Dung", "Trần", 3.27),
        Student("SV1010", "Chi", "Mai", 3.09),
        Student("SV1011", "Phương", "Ma", 3.45)
    ]
    stack = Stack()
    # thêm các phần tử vào stack
    for element in students:
        stack.push(element)
    print(f'==> Số phần tử trong stack: {stack.size()}')
    print(f'==> Stack đầy? {stack.is_full()}')
    # lấy phần tử đầu stack
    print(f'==> Phần tử đầu stack: {stack.top()}')
    # xóa phần tử đầu stack
    print('SAU KHI XÓA MỘT PHẦN TỬ KHỎI STACK: ')
    stack.pop()
    print(f'==> Số phần tử trong stack: {stack.size()}')
    print(f'==> Phần tử đầu stack: {stack.top()}')
    print('CÁC PHẦN TỬ CÒN LẠI TRONG STACK: ')
    print('==> Các phần tử trong stack: ')
    show_stack_elements(stack)

    # pop thử stack sau khi stack rỗng
    print('CÁC THAO TÁC KHI STACK RỖNG: ')
    stack.pop()
    print(f'==> Số phần tử trong stack: {stack.size()}')
    print(f'==> Phần tử đầu stack: {stack.top()}')


if __name__ == '__main__':
    test()
