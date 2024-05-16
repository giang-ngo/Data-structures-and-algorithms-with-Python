# lớp mô tả thông tin một node của danh sách liên kết
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


# lớp mô tả thông tin danh sách liên kết vòng
class CircularLinkedList:
    def __init__(self):
        self.__tail = None
        self.__head = None

    # phương thức thêm node mới vào DSLK vòng
    def insert(self, data):
        p = Node(data)  # tạo mới một node với dữ liệu cho trước
        if self.is_empty():  # nếu danh sách rỗng
            self.__head = self.__tail = p  # head và tail trùng nhau
            p.next = self.__head  # next của p là head
            p.prev = self.__head  # prev của p cũng là head
        else:  # nếu danh sách không rỗng
            p.next = self.__head  # gán next của p
            self.__head.prev = p  # gán prev của head
            p.prev = self.__tail  # gán prev của p là tail
            self.__tail.next = p  # gán next của tail là p
            self.__head = p  # cập nhật lại head là p

    # phương thức xóa node khỏi danh sách liên kết vòng
    def remove(self) -> bool:
        if self.is_empty():  # nếu danh sách rỗng
            return False  # không có gì để xóa
        # r = self.__head  # lưu lại node cần xóa
        if self.__head.next == self.__head:  # nếu danh sách chỉ có 1 node
            self.__head = None
            self.__tail = None
        else:  # trường hợp danh sách có nhiều node
            self.__head = self.__head.next
            self.__head.prev = self.__tail
            self.__tail.next = self.__head
        # del r  # xóa node r
        return True  # trả về thông báo xóa thành công

    # phương thức dùng để kiểm tra DSLK có rỗng không
    def is_empty(self):
        return self.__head is None

    # phương thức duyệt các node trong danh sách
    def show_elements(self):
        if self.is_empty():
            print('==> Danh sách rỗng.')
        else:
            p = self.__head  # xuất phát từ node cuối của trong DSLK
            while p is not None:  # lặp chừng nào chưa hết danh sách
                print(f'{p.data} -> ', end='')  # in ra giá trị của node đang xét
                p = p.next  # chuyển sang node liền trước
                if p == self.__head:  # kết thúc một vòng
                    break  # ngắt việc duyệt
            print('None')


# hàm kiểm tra việc thực thi các chức năng
def test():
    circular_linked_list = CircularLinkedList()
    # thêm các node vào DSLK vòng
    circular_linked_list.insert("Mai")
    circular_linked_list.insert("Loan")
    circular_linked_list.insert("Khoa")
    circular_linked_list.insert("Linh")
    circular_linked_list.insert("Long")
    circular_linked_list.insert("Trang")
    circular_linked_list.insert("Huy")
    print('==> DSLK vòng sau khi thêm các node mới: ')
    circular_linked_list.show_elements()

    # xóa phần tử khỏi danh sách liên kết vòng
    circular_linked_list.remove()
    print('==> DSLK vòng sau khi xóa một node: ')
    circular_linked_list.show_elements()


if __name__ == '__main__':
    test()
