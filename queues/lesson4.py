# lớp mô tả thông tin một node
class Node:
    def __init__(self, data=None, priority=0):
        self.__data = data  # dữ liệu của node
        self.__priority = priority  # thứ tự ưu tiên
        self.__next = None  # địa chỉ node kế tiếp

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

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        self.__priority = value


# lớp mô tả queues và các hành động
class PriorityQueue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # phương thức thêm node vào cuối queues
    def push(self, value, priority):
        new_node = Node(value, priority)
        if self.is_empty():
            self.__head = self.__tail = new_node
        elif priority > self.__head.priority:
            new_node.next = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if current == self.__tail:
                self.__tail = new_node
        self.__size += 1

    # phương thức xóa node đầu queues
    def pop(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        value = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return value

    # phương thức trả về node đầu queues
    def front(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        return self.__head.data

    # phương thức trả về node cuối queues
    def back(self):
        if self.is_empty():
            print('Queue is empty')
            return None
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
            print(f'({p.data}, p={p.priority}) -> ')  # in ra giá trị của node đang xét
            p = p.next  # chuyển sang node kế tiếp
        print('None')  # cuối cùng khi đã in xong in ra None => kết thúc DSLK


if __name__ == '__main__':
    queue = PriorityQueue()
    # thêm các node vào đầu DSLK
    queue.push("Mai", 5)
    queue.push("Loan", 1)
    queue.push("Khoa", 7)
    queue.push("Linh", 9)
    queue.push("Long", 2)
    queue.push("Trang", 8)
    queue.push("Minh", 9)
    queue.push("Nga", 6)
    queue.push("Huy", 3)
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
