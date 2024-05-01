from linked_list.lesson6.student import Student


# lớp mô tả thông tin về một node
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


# lớp mô tả danh sách liên kết
class LinkedList:
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
            p = self.__head  # gọi p là node trước node cuối
            while p.next != r:  # tìm node p
                p = p.next
            p.next = None
            self.__tail = p
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
            prev_x = self.__head  # prev_p là node trước node p
            while p is not None:  # tìm node có giá trị x
                if p.data == x:
                    break
                prev_x = p
                p = p.next
            if p is not None:
                prev_x.next = p.next  # cập nhật node next của prev_x
                del p  # xóa bỏ node p
                return True  # trả về kết quả xóa thành công
            else:
                return False  # không tìm thấy node cần xóa

    def sort(self, reverse=False):
        if reverse:
            self.sort_desc()
        else:
            self.sort_asc()

    def sort_asc(self):  # phương thức sắp xếp tăng dần
        p = self.__head
        while p is not None:
            q = p.next
            while q is not None:
                if q.data < p.data:
                    p.data, q.data = q.data, p.data  # tráo đổi
                q = q.next
            p = p.next

    def sort_desc(self):  # phương thức sắp xếp giảm dần
        p = self.__head
        while p is not None:
            q = p.next
            while q is not None:
                if q.data > p.data:  # nếu dữ liệu node q lớn hơn node p
                    p.data, q.data = q.data, p.data  # tráo đổi
                q = q.next
            p = p.next


# hàm chứa thông tin để chạy kiểm tra kết quả triển khai dslk
def test():
    # tạo dữ liệu ban đầu
    students = [
        Student("SV1001", "Nam", "Hoàng", 3.26),
        Student("SV1002", "Hoa", "Lương", 3.36),
        Student("SV1003", "Bách", "Ngô", 3.21),
        Student("SV1004", "Trung", "Trần", 3.54),
        Student("SV1005", "Loan", "Lê", 3.04),
        Student("SV1006", "Mai", "Nguyễn", 3.87),
        Student("SV1007", "Khoa", "Lê", 3.71),
        Student("SV1008", "Ánh", "Nguyễn", 3.64),
        Student("SV1009", "Dung", "Trần", 3.27)
    ]
    linked_list_students = LinkedList()
    for student in students:
        linked_list_students.insert_tail(student)

    # in ra danh sách trước khi cập nhật
    print('==> DSLK trước khi sắp xếp: ')
    linked_list_students.show_elements()

    # sắp xếp tăng dần theo điểm sv
    msg = '==> DSLK sau khi sắp xếp theo điểm SV tăng dần.'
    print(msg)
    linked_list_students.sort()
    linked_list_students.show_elements()

    # sắp xếp giảm dần theo điểm sv
    msg = '==> DSLK sau khi sắp xếp theo điểm SV giảm dần.'
    print(msg)
    linked_list_students.sort(reverse=True)
    linked_list_students.show_elements()


# hàm main
if __name__ == '__main__':
    test()
