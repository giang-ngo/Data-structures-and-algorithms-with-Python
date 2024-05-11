from queues.student import Student


# lớp mô tả một queues và các hành động của nó
class Queue:
    # hàm khởi tạo
    def __init__(self, capacity=0):
        self.__data: list = []
        self.__capacity: int  # số phần tử tối đa có thể chứa
        self.__size: int = 0  # số phần tử thực tế hiện thời
        # giả định rằng capacity khi không chỉ định là 10
        if capacity <= 0:
            self.__capacity = 10
        else:  # nếu không sẽ lấy giá trị được gửi vào
            self.__capacity = capacity

    # phương thức kiểm tra queues rỗng
    def is_empty(self):
        return self.__size == 0

    # phương thức thêm mới phần tử vào queues
    def push(self, value) -> bool:
        if self.is_full():
            print('==> Queue đầy. Thêm thất bại.')
            return False
        else:
            self.__data.append(value)  # thêm phần tử mới vào cuối list
            self.__size += 1  # tăng size lên 1
            return True

    # phương thức xóa bỏ phần tử đầu queues
    def pop(self):
        if self.is_empty():  # queues rỗng, không có gì để xóa
            print('==> Queue rỗng')
            return None
        else:  # nếu queues có phần tử
            element = self.__data.pop(0)  # pop phần tử ở đầu list
            self.__size -= 1  # giảm số lượng phần tử đi 1
            return element

    # phương thức lấy ra phần tử ở đầu queues
    def front(self):
        if self.is_empty():
            print('==> Queue rỗng')
            return None
        else:
            element = self.__data[0]
            return element

    # phương thức lấy ra phần tử ở cuối queues
    def back(self):
        if self.is_empty():
            print('==> Queue rỗng')
            return None
        else:
            element = self.__data[self.__size - 1]
            return element

    # phương thức trả về kích thước hiện thời
    def size(self):
        return self.__size

    # phương thức kiểm tra queues đã đầy chưa
    def is_full(self):
        return self.__size == self.__capacity

    # phương thức hiển thị các phần tử trong queues
    def show_elements(self):
        for item in self.__data:
            print(item)


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
    queue = Queue()
    # pop thử queues sau khi queues rỗng
    print('CÁC THAO TÁC KHI QUEUE RỖNG: ')
    queue.pop()
    print(f'==> Số phần tử trong queues: {queue.size()}')
    print(f'==> Phần tử đầu queues: {queue.front()}')
    print(f'==> Phần tử cuối queues: {queue.back()}')

    # thêm các phần tử vào queues
    print('SAU KHI THÊM CÁC PHẦN TỬ VÀO QUEUE: ')
    for element in students:
        queue.push(element)
    print(f'==> Số phần tử trong queues: {queue.size()}')
    print(f'==> Queue đầy? {queue.is_full()}')
    # lấy phần tử hai đầu queues
    print(f'==> Phần tử đầu queues: {queue.front()}')
    print(f'==> Phần tử cuối queues: {queue.back()}')

    # xóa phần tử đầu queues
    print('SAU KHI XÓA MỘT PHẦN TỬ KHỎI QUEUE: ')
    queue.pop()
    print(f'==> Số phần tử trong queues: {queue.size()}')
    print(f'==> Phần tử đầu queues: {queue.front()}')
    print(f'==> Phần tử cuối queues: {queue.back()}')
    print('CÁC PHẦN TỬ CÒN LẠI TRONG QUEUE: ')
    print('==> Các phần tử trong queues: ')
    queue.show_elements()


if __name__ == '__main__':
    test()
