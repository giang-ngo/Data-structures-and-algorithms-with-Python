from linked_list.student import Student


# lớp mô tả thông tin một node
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


# lớp mô tả danh sách liên kết
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
            print(f'{p.data} -> ')  # in ra giá trị của node đang xét
            p = p.next  # chuyển sang node kế tiếp
        print('None')  # cuối cùng khi đã in xong in ra None => kết thúc DSLK

    # phương thức duyệt danh sách từ cuối lên đầu
    def show_elements_reverse(self):
        p = self.__tail  # xuất phát từ node cuối của trong DSLK
        while p is not None:  # lặp chừng nào chưa hết danh sách
            print(f'{p.data} -> ')  # in ra giá trị của node đang xét
            p = p.prev  # chuyển sang node liền trước
        print('None')  # cuối cùng khi đã in xong in ra None => kết thúc DSLK

    # phương thức cập nhật điểm cho một đối tượng sinh viên
    def update_gpa(self, student: Student) -> bool:
        p = self.__head
        while p is not None:
            if p.data == student:
                p.data.gpa = student.gpa
                return True
            p = p.next
        return False

    # phương thức xóa phần tử ở đầu danh sách liên kết
    def remove_head(self) -> bool:
        if self.is_empty():  # trường hợp danh sách rỗng
            return False  # không có gì để xóa
        elif self.__head == self.__tail:  # trường hợp danh sách chỉ có 1 node
            r = self.__head
            self.__head = None
            self.__tail = None
            del r
            return True
        else:  # trường hợp danh sách có nhiều node
            r = self.__head  # lưu lại head cũ ra một biến tạm
            self.__head = self.__head.next  # cập nhật head mới
            self.__head.prev = None  # cập nhật tham chiếu tới node liền trước
            del r  # xóa bỏ node head cũ
            return True  # trả về kết quả xóa thành công

    # phương thức xóa node cuối danh sách liên kết
    def remove_tail(self):
        if self.is_empty():  # trường hợp danh sách rỗng
            return False
        elif self.__head == self.__tail:  # trường hợp danh sách chỉ có 1 node
            return self.remove_head()
        else:  # trường hợp
            r = self.__tail  # lưu lại node cuối cần xóa
            p = self.__tail.prev  # gọi p là node trước node cuối
            p.next = None  # cập nhật node liền sau của p
            self.__tail = p
            r.prev = None  # cập nhật node liền trước của r
            del r
            return True  # trả về kết quả xóa thành công

    # phương thức xóa node x bất kỳ
    def remove(self, x):
        if self.is_empty():  # nếu danh sách rỗng
            return False
        elif self.__head.data == x:  # nếu node cần xóa là node đầu
            return self.remove_head()
        elif self.__tail.data == x:  # nếu node cần xóa là node cuối
            return self.remove_tail()
        else:  # lúc này node x không phải node đầu hoặc node cuối
            p = self.__head  # p là node cần xóa
            while p is not None:  # tìm node có giá trị x
                if p.data == x:
                    break
                p = p.next
            if p is not None:
                prev_p = p.prev  # prev_p là node trước node p
                prev_p.next = p.next  # cập nhật node next của prev_p
                p.next.prev = prev_p  # cập nhật node liền trước của node sau node p
                del p  # xóa bỏ node p
                return True  # trả về kết quả xóa thành công
            else:  # node x không tồn tại
                return False  # không tìm thấy node cần xóa


# hàm hiển thị kết quả xóa
def show_result(list_students: DoublyLinkedList, del_result: bool, msg: str):
    if del_result:
        print(msg)
        list_students.show_elements()
        print('==> DSLK duyệt ngược: ')
        list_students.show_elements_reverse()
    else:
        print('==> Xóa node thất bại.')


# hàm chứa thông tin để chạy kiểm tra kết quả triển khai dslk
def test():
    # tạo dữ liệu ban đầu
    students = [
        Student("SV1001", "Nam", "Hoàng", 3.26),
        Student("SV1002", "Hoa", "Lương", 3.36),
        Student("SV1003", "Bách", "Ngô", 3.21),
        Student("SV1004", "Trung", "Trần", 3.54),
        Student("SV1005", "Loan", "Lê", 3.04),
        Student("SV1006", "Mai", "Nguyễn", 3.87)
    ]
    linked_list_students = DoublyLinkedList()
    for student in students:
        linked_list_students.insert_tail(student)

    # in ra danh sách trước khi cập nhật
    print('==> DSLK trước khi cập nhật: ')
    linked_list_students.show_elements()

    # tiến hành xóa node đầu danh sách
    del_result = linked_list_students.remove_head()
    msg = '==> Xóa thành công node đầu danh sách.'
    show_result(linked_list_students, del_result, msg)

    # tiến hành xóa node cuối danh sách
    del_result = linked_list_students.remove_tail()
    msg = '==> Xóa thành công node cuối danh sách.'
    show_result(linked_list_students, del_result, msg)

    # xóa node bất kỳ
    x = Student(student_id='SV1002')
    del_result = linked_list_students.remove(x)
    msg = '==> Xóa thành công node bất kỳ trong danh sách.'
    show_result(linked_list_students, del_result, msg)
    # xóa một node không tồn tại trong danh sách
    x = Student(student_id='SV1001')
    del_result = linked_list_students.remove(x)
    show_result(linked_list_students, del_result, msg)


# hàm main
if __name__ == '__main__':
    test()
