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


# lớp mô tả queues và các hành động
class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # phương thức thêm node vào cuối queues
    def push(self, data):
        p = Node(data)  # tạo mới một node với dữ liệu cho trước
        if self.is_empty():  # nếu danh sách rỗng
            self.__head = p
            self.__tail = p
        else:  # nếu danh sách không rỗng
            self.__tail.next = p
            self.__tail = p  # cập nhật lại node tail
        self.__size += 1

    # phương thức xóa node đầu queues
    def pop(self):
        if self.is_empty():
            print('==> Queue rỗng')
            return None
        else:
            p = self.__head
            value = p.data
            self.__head = self.__head.next
            self.__size -= 1
            del p
            return value

    # phương thức trả về node đầu queues
    def front(self):
        if self.is_empty():
            print('==> Queue rỗng')
            return None
        else:
            return self.__head.data

    # phương thức trả về node cuối queues
    def back(self):
        if self.is_empty():
            print('==> Queue rỗng')
            return None
        else:
            return self.__tail.data

    # phương thức dùng để kiểm tra DSLK có rỗng không
    def is_empty(self):
        return self.__size == 0

    # phương thức trả về số phần tử hiện có trong queues
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
    queue = Queue()
    # thêm các node vào đầu DSLK
    queue.push("Mai")
    queue.push("Loan")
    queue.push("Khoa")
    queue.push("Linh")
    queue.push("Long")
    queue.push("Trang")
    queue.push("Huy")
    print('==> Queue sau khi thêm các node vào queues: ')
    queue.show_elements()
    print(f'==> Số lượng phần tử trong queues: {queue.size()}')
    print(f'==> Phần tử đầu queues: {queue.front()}')
    print(f'==> Phần tử cuối queues: {queue.back()}')

    # xóa phần tử top
    queue.pop()
    print('SAU KHI XÓA PHẦN TỬ ĐẦU QUEUE: ')
    print(f'==> Số lượng phần tử trong queues: {queue.size()}')
    print(f'==> Phần tử đầu queues: {queue.front()}')
    print(f'==> Phần tử cuối queues: {queue.back()}')

    # hiển thị các phần tử còn lại của queues
    print('==> Các phần tử trong queues theo thứ tự đầu -> cuối: ')
    queue.show_elements()
