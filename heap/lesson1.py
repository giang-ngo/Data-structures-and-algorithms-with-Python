class Heap:
    """ Class representing a max-heap. """

    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__size = 0
        self.__data = [0] * self.__capacity

    def insert(self, value):
        """ Phương thức thêm mới phần tử vào heap. """
        if self.__size == self.__capacity:
            self.__resize()
        self.__data[self.__size] = value
        self.__sift_up(self.__size)
        self.__size += 1

    def show_elements(self):
        """ Phương thức hiển thị các phần tử của heap. """
        if self.is_empty():
            print('==> Heap is empty.')
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

    def __sift_up(self, index):
        """ Phương thức vun đống(sàng) lên. """
        while index > 0:
            parent_index = (index - 1) // 2
            if self.__data[index] > self.__data[parent_index]:
                self.__data[index], self.__data[parent_index] = self.__data[parent_index], self.__data[index]
                index = parent_index
            else:
                break

    def __resize(self):
        """ Thay đổi kích thước bộ nhớ trong của heap. """
        self.__capacity *= 2
        new_data = [0] * self.__capacity
        for i in range(self.__size):
            new_data[i] = self.__data[i]
        self.__data = new_data


def test():
    # tạo heap mới
    heap = Heap()
    # thêm các phần tử vào heap
    heap.insert(20)
    heap.insert(40)
    heap.insert(10)
    heap.insert(90)
    heap.insert(30)
    heap.insert(50)
    # hiển thị thông tin về heap:
    print(f'==> Heap rỗng? {heap.is_empty()}')
    print(f'==> Số phần tử trong heap: {heap.size()}')
    print('==> Các phần tử trong heap:')
    h
    heap.show_elements()


if __name__ == '__main__':
    test()
