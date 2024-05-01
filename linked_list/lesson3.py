from linked_list.student import Student

# lớp mô tả thông tin về một node
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


# lớp mô tả danh sách liên kết đơn
class LinkedList:
    def __init__(self):
        self.__tail = None  # node cuối
        self.__head = None  # node đầu

    # phương thức thêm node mới vào đầu DSLK
    def insert_head(self, data):
        p = Node(data)  # tạo mới một node với dữ liệu cho trước
        if self.is_empty():  # nếu danh sách rỗng
            self.__head = self.__tail = p
        else:  # nếu danh sách không rỗng
            p.next = self.__head
            self.__head = p

    # phương thức thêm node mới vào cuối DSLK
    def insert_tail(self, data):
        if self.is_empty():
            self.insert_head(data)
        else:
            p = Node(data)  # tạo node
            self.__tail.next = p  # cập nhật next của tail cũ
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
            print(f'{p.data} -> ')  # in ra node đang xét trên 1 dòng
            p = p.next  # chuyển sang node kế tiếp
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
    linked_list_students = LinkedList()
    for student in students:
        linked_list_students.insert_tail(student)

    # in ra danh sách trước khi cập nhật
    print('==> DSLK trước khi cập nhật: ')
    linked_list_students.show_elements()

    # tiến hành cập nhật
    student = Student(student_id='SV1005', gpa=3.77)
    update_result = linked_list_students.update_gpa(student)
    if update_result:
        print(f'==> Sau khi cập nhật điểm cho SV mã "{student.student_id}": ')
        linked_list_students.show_elements()
    else:
        print(f'==> Không tồn tại sinh viên mã "{student.student_id}".')


if __name__ == '__main__':
    test()
