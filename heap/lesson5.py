class HeapNode:
    def __init__(self, data=None, priority=0):
        self.__data = data
        self.__priority = priority

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        self.__priority = value

    def __lt__(self, other):  # nạp chồng toán tử <
        return self.priority < other.priority

    def __gt__(self, other):  # nạp chồng toán tử >
        return self.priority > other.priority

    def __eq__(self, other):  # nạp chồng toán tử ==
        return self.data == other.data

    def __str__(self):
        return f'({self.data}, {self.priority})'


class PriorityQueue:
    """ Lớp mô tả thông tin và hành động của hàng đợi ưu tiên tạo bởi heap. """

    def __init__(self, capacity=0):
        self.__capacity = max(10, capacity)
        self.__size: int = 0
        self.__data: list = [0] * self.__capacity

    def push_node(self, value=None, priority=0):
        """ Phương thức thêm mới một nút vào hàng đợi ưu tiên. """
        if self.__size >= self.__capacity:
            self.__data.append(HeapNode(value, priority))
            self.__capacity += 1
        else:
            self.__data[self.__size] = HeapNode(value, priority)
        self.sift_up(self.__size)
        self.__size += 1
        return True

    def show_elements(self):
        """ Phương thức hiển thị các phần tử của hàng đợi. """
        print(*self.__data[:self.__size], sep=', ')

    def size(self):
        """ Phương thức trả về kích thước hiện thời của hàng đợi. """
        return self.__size

    def is_empty(self):
        """ Phương thức kiểm tra xem hàng đợi có rỗng không. """
        return self.__size == 0

    def sift_up(self, index):
        """ Phương thức vun đống(sàng) lên. """
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.__data[index] > self.__data[parent_index]:
            self.__data[index], self.__data[parent_index] = self.__data[parent_index], self.__data[index]
            self.sift_up(parent_index)

    def sift_down(self, index):
        """ Phương thức sàng xuống. """
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < self.__size and self.__data[left] > self.__data[largest]:
            largest = left
        if right < self.__size and self.__data[right] > self.__data[largest]:
            largest = right
        if largest != index:
            self.__data[index], self.__data[largest] = self.__data[largest], self.__data[index]
            self.sift_down(largest)

    def pop(self) -> HeapNode | None:
        """ Phương thức xóa bỏ và trả về phần tử có độ ưu tiên cao nhất từ hàng đợi. """
        if not self.is_empty():
            tmp = self.__data[0]
            self.__size -= 1
            self.sift_down(0)
            return tmp
        else:
            return None

    def front(self) -> HeapNode | None:
        """ Phương thức lấy và trả về phần tử đầu hàng đợi. """
        return self.__data[0] if not self.is_empty() else None

    def back(self):
        """Lấy và trả về phần tử cuối hàng đợi."""
        return self.__data[self.__size - 1] if not self.is_empty() else None


def test():
    # tạo hàng đợi mới
    priority_queue = PriorityQueue()
    # thêm các phần tử vào hàng đợi
    priority_queue.push_node(20, 2)
    priority_queue.push_node(40, 5)
    priority_queue.push_node(10, 6)
    priority_queue.push_node(90, 1)
    priority_queue.push_node(30, 7)
    priority_queue.push_node(50, 8)
    priority_queue.push_node(80, 10)
    priority_queue.push_node(15, 3)
    priority_queue.push_node(70, 4)

    # hiển thị thông tin về hàng đợi:
    print(f'==> Số phần tử trong hàng đợi {priority_queue.size()}')
    print('==> Các phần tử trong hàng đợi: ')
    priority_queue.show_elements()
    print(f'==> Phần tử đầu hàng đợi: {priority_queue.front()}')
    print(f'==> Phần tử cuối hàng đợi: {priority_queue.back()}')


if __name__ == '__main__':
    test()
