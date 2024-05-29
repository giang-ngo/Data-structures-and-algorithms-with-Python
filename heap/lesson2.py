class Heap:
    """ Lớp mô tả thông tin và hành động của heap. """

    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__size: int = 0
        self.__data: list = [-999999] * self.__capacity

    def insert(self, value):
        """ Phương thức thêm mới phần tử vào heap. """
        if self.__size < self.__capacity:
            self.__data[self.__size] = value
            self.sift_up(self.__size)
            self.__size += 1
            return True
        else:
            return False

    def show_elements(self):
        """ Phương thức hiển thị các phần tử của heap. """
        if self.is_empty():
            print('==> Heap rỗng.')
        else:
            for i in range(self.__size):
                print(f'{self.__data[i]} ', end='')
        print()

    def size(self):
        """ Phương thức trả về kích thước hiện thời của heap. """
        return self.__size

    def is_empty(self):
        """ Phương thức kiểm tra xem heap có rỗng không. """
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

    def find_node_index(self, value):
        """ Phương thức tìm vị trí của phần tử trong heap. """
        try:
            return self.__data.index(value)
        except ValueError:
            return -1

    def remove(self, value):
        """ Phương thức xóa bỏ phần tử có giá trị value cho trước. """
        index = self.find_node_index(value)
        if index >= 0:
            self.__data[index] = self.__data[self.__size - 1]
            self.__size -= 1
            self.sift_down(index)
            return True
        else:
            return False


def test():
    heap = Heap()
    heap.insert(20)
    heap.insert(40)
    heap.insert(10)
    heap.insert(90)
    heap.insert(30)
    heap.insert(50)
    heap.insert(80)
    heap.insert(15)
    heap.insert(70)
    print(f'==> Heap rỗng? {heap.is_empty()}')
    print(f'==> Số phần tử trong heap {heap.size()}')
    print('==> Các phần tử trong heap: ')
    heap.show_elements()

    heap.remove(70)
    print('==> Các phần tử trong heap sau khi xóa: ')
    heap.show_elements()


if __name__ == '__main__':
    test()
