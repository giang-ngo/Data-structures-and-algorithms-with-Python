class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None
        self.__prev = None

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
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value


class DoublyLinkedList:
    def __init__(self):
        self.__tail = None
        self.__head = None

    # phương thức thêm node mới vào đầu DSLK
    def insert_head(self, data):
        p = Node(data)  # tạo mới một node với dữ liệu cho trước
        if self.is_empty():  # nếu danh sách rỗng
            self.__head = self.__tail = p
        else:  # nếu danh sách không rỗng
            p.next = self.__head
            self.__head.prev = p
            self.__head = p

    # phương thức thêm node mới vào cuối DSLK
    def insert_tail(self, data):
        if self.is_empty():
            self.insert_head(data)
        else:
            p = Node(data)  # tạo node
            self.__tail.next = p  # cập nhật next của tail cũ
            p.prev = self.__tail  # cập nhật node prev của p
            self.__tail = p  # cập nhật lại tail mới

    # phương thức thêm node mới vào sau node có giá trị x
    def insert_after_x(self, data, x):
        node_x = self.__head  # giả sử node có giá trị x là node head
        while node_x is not None:  # lặp chừng nào chưa hết danh sách
            if node_x.data == x:  # nếu tìm thấy
                break  # kết thúc việc tìm node có giá trị x
            node_x = node_x.next  # xét node kế tiếp
        if node_x is not None:  # nếu tìm thấy node có giá trị x
            if node_x == self.__tail:
                self.insert_tail(data)
            else:
                p = Node(data)  # tạo node
                p.next = node_x.next  # cập nhật next của p
                p.prev = node_x  # cập nhật prev của p
                if node_x.next is not None:
                    node_x.next.prev = p  # cập nhật prev của node sau node x
                node_x.next = p  # cập nhật lại next của node x
        else:  # nếu không tìm thấy
            print('==> Không tìm thấy node mục tiêu.')

    # phương thức dùng để kiểm tra DSLK có rỗng không
    def is_empty(self):
        return self.__head is None

    # phương thức dùng để hiển thị các phần tử trong DSLK
    def show_elements(self):
        p = self.__head  # xuất phát từ node đầu tiên trong DSLK
        while p is not None:  # lặp chừng nào chưa hết danh sách
            print(f'{p.data} -> ', end='')  # in ra giá trị của node đang xét
            p = p.next  # chuyển sang node kế tiếp
        print('None')  # cuối cùng khi đã in xong in ra None => kết thúc DSLK

    # phương thức duyệt danh sách từ cuối lên đầu
    def show_elements_reverse(self):
        p = self.__tail  # xuất phát từ node cuối của trong DSLK
        while p is not None:  # lặp chừng nào chưa hết danh sách
            print(f'{p.data} -> ', end='')  # in ra giá trị của node đang xét
            p = p.prev  # chuyển sang node liền trước
        print('None')  # cuối cùng khi đã in xong in ra None => kết thúc DSLK


def test():
    linked_list = DoublyLinkedList()
    # thêm các node vào đầu DSLK
    linked_list.insert_head("Mai")
    linked_list.insert_head("Loan")
    linked_list.insert_head("Khoa")
    linked_list.insert_head("Linh")
    print('==> DSLK sau khi thêm các node vào đầu: ')
    linked_list.show_elements()
    print('==> DSLK khi duyệt ngược: ')
    linked_list.show_elements_reverse()

    # thêm các node vào cuối
    linked_list.insert_tail("Long")
    linked_list.insert_tail("Trang")
    linked_list.insert_tail("Huy")
    print('==> DSLK sau khi thêm các node vào cuối: ')
    linked_list.show_elements()
    print('==> DSLK khi duyệt ngược: ')
    linked_list.show_elements_reverse()

    # thêm các node vào sau một node nào đó
    name = input('Nhập tên cần thêm vào DSLK: ')
    x = input('Nhập tên người chọn làm mốc: ')
    linked_list.insert_after_x(name, x)
    print(f'==> DSLK sau khi chèn {name} vào sau node có giá trị {x}: ')
    linked_list.show_elements()
    print('==> DSLK khi duyệt ngược: ')
    linked_list.show_elements_reverse()


if __name__ == '__main__':
    test()