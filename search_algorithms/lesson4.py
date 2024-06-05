import sys

class Entry:
    """ Lớp biểu diễn một phần tử dữ liệu của bảng băm. """
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.hash = self.hash_code()

    def hash_code(self):
        """ Phương thức băm tạo mã băm cho một key. """
        return sum(ord(c) * pow(31, len(self.key) - i - 1) for i, c in enumerate(self.key))

    def __str__(self):
        return f'[{self.key} - {self.value}]'

    def __eq__(self, other):
        return isinstance(other, Entry) and self.hash == other.hash

class HashTable:
    """ Lớp mô tả bảng băm. """
    def __init__(self, capacity=10):
        self.capacity = max(1, capacity)
        self.table = [[] for _ in range(self.capacity)]
        self.MAX_SIZE = sys.maxsize - 8
        self._load_factor = 0.75
        self.__threshold = int(self.capacity * self._load_factor)
        self.__count = 0

    def hash_code(self, code):
        """ Trả về chỉ số của danh sách chứa phần tử với mã băm cho trước. """
        return code % self.capacity

    def insert(self, key, value):
        """ Chèn phần tử mới vào bảng băm. """
        if self.__count >= self.__threshold:
            self.rehash()
        entry = Entry(key, value)
        index = self.hash_code(entry.hash)
        self.table[index].append(entry)
        self.__count += 1

    def update(self, key, new_value):
        """ Cập nhật một phần tử nào đó trong bảng băm. """
        entry = Entry(key)
        index = self.hash_code(entry.hash)
        for element in self.table[index]:
            if element == entry:
                element.value = new_value
                return True
        return False

    def rehash(self):
        """ Băm lại bảng băm để tăng gấp đôi dung lượng. """
        old_table = self.table
        self.capacity = min((self.capacity << 1) + 1, self.MAX_SIZE)
        self.table = [[] for _ in range(self.capacity)]
        self.__threshold = min(int(self.capacity * self._load_factor), self.MAX_SIZE + 1)
        self.__count = 0
        for bucket in old_table:
            for entry in bucket:
                self.insert(entry.key, entry.value)

    def keys(self):
        """ Trả về danh sách các khóa trong bảng băm. """
        return [entry.key for bucket in self.table for entry in bucket]

    def values(self):
        """ Trả về danh sách các giá trị trong bảng băm. """
        return [entry.value for bucket in self.table for entry in bucket]

    def entries(self):
        """ Trả về danh sách các phần tử trong bảng băm. """
        return [entry for bucket in self.table for entry in bucket]

    def get(self, key):
        """ Trả về giá trị ứng với khóa cho trước. """
        entry = Entry(key)
        index = self.hash_code(entry.hash)
        for element in self.table[index]:
            if element == entry:
                return element.value
        return None

    def contains_key(self, key):
        """ Kiểm tra xem khóa có tồn tại không. """
        return self.get(key) is not None

    def contains_value(self, value):
        """ Kiểm tra xem giá trị có tồn tại không. """
        return any(value == entry.value for bucket in self.table for entry in bucket)

    def display(self):
        """ Hiển thị các phần tử trong bảng băm. """
        for i, bucket in enumerate(self.table):
            print(f'[{i}]: ', end='')
            for entry in bucket:
                print(f'--> {entry}', end=' ')
            print()

def print_data(data):
    """ Hiển thị các entry/key/value của bảng băm. """
    for item in data:
        print(item)

if __name__ == '__main__':
    hash_table = HashTable(25)
    entries = [
        ("Hello", "Xin chào"), ("Love", "Yêu thương"), ("Baby", "Em bé"),
        ("Mother", "Mẹ"), ("Lovely", "Đáng yêu"), ("Ugly", "Xấu xí"),
        ("Chicken", "Con gà"), ("Kitty", "Mèo con"), ("Piggy", "Heo con"),
        ("Puppy", "Cún con"), ("Father", "Cha"), ("Flower", "Bông hoa"),
        ("Fruit", "Trái cây"), ("Happy", "Sung sướng"), ("Banana", "Quả chuối"),
        ("Monkey", "Con khỉ"), ("Freeze", "Đóng băng")
    ]
    for key, value in entries:
        hash_table.insert(key, value)

    print('==> Thông tin trong bảng băm: ')
    hash_table.display()

    keys_to_search = ["Kitty", "Lovely", "Quobee", "Mommy"]
    for key in keys_to_search:
        print(f'==> Giá trị ứng với key "{key}": ')
        print(hash_table.get(key))

    keys_to_check = ["Hello", "Good"]
    for key in keys_to_check:
        print(f'==> Key "{key}" có tồn tại trong bảng băm không? {hash_table.contains_key(key)}')

    values_to_check = ["Con khỉ", "Bla bla"]
    for value in values_to_check:
        print(f'==> Value "{value}" có tồn tại trong bảng băm không? {hash_table.contains_value(value)}')
