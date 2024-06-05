import sys


class Entry:
    """Lớp biểu diễn một phần tử dữ liệu của bảng băm."""

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.hash = self.hash_code()

    def hash_code(self):
        """Phương thức băm tạo mã băm cho một key."""
        result = 0
        n = len(self.key)
        for i, c in enumerate(self.key):
            result += ord(c) * (31 ** (n - i - 1))
        return result

    def __str__(self):
        return f'[{self.key} - {self.value}]'


class HashTable:
    """Lớp mô tả bảng băm."""

    def __init__(self, capacity=10):
        """Hàm khởi tạo."""
        self.capacity = max(10, capacity)
        self.table = [[] for _ in range(self.capacity)]
        self.MAX_SIZE = sys.maxsize - 8
        self._load_factor = 0.75
        self.__mod_count = 0
        self.__threshold = int(self.capacity * self._load_factor)
        self.__count = 0

    def hash_code(self, code):
        """Phương thức trả về chỉ số của danh sách chứa phần tử với mã băm cho trước."""
        return code % self.capacity

    def insert(self, key, value):
        """Phương thức chèn phần tử mới vào bảng băm."""
        if self.__count >= self.__threshold:
            self.rehash()
        entry = Entry(key, value)
        index = self.hash_code(entry.hash)
        self.table[index].append(entry)
        self.__count += 1
        self.__mod_count += 1

    def update(self, key, new_value):
        """Phương thức cập nhật một phần tử nào đó trong bảng băm."""
        entry = Entry(key, new_value)
        index = self.hash_code(entry.hash)
        for element in self.table[index]:
            if element.hash == entry.hash:
                element.value = new_value
                return True
        return False

    def rehash(self):
        """Phương thức băm lại bảng băm."""
        old_capacity = self.capacity
        old_table = self.table
        new_capacity = (old_capacity << 1) + 1
        if new_capacity - self.MAX_SIZE > 0:
            if old_capacity >= self.MAX_SIZE:
                return
            new_capacity = self.MAX_SIZE

        self.table = [[] for _ in range(new_capacity)]
        self.capacity = new_capacity
        self.__mod_count += 1
        self.__threshold = min(int(new_capacity * self._load_factor), self.MAX_SIZE + 1)

        for bucket in old_table:
            for element in bucket:
                index = self.hash_code(element.hash)
                self.table[index].append(element)

    def keys(self):
        """Phương thức lấy và trả về danh sách các khóa trong cặp key-value."""
        return [item.key for bucket in self.table for item in bucket]

    def values(self):
        """Phương thức lấy và trả về danh sách các giá trị trong cặp key-value."""
        return [item.value for bucket in self.table for item in bucket]

    def entries(self):
        """Phương thức lấy danh sách các entry của bảng băm."""
        return [item for bucket in self.table for item in bucket]

    def display(self):
        """Phương thức hiển thị các phần tử trong bảng băm."""
        for i, bucket in enumerate(self.table):
            print(f'[{i}]: ', end='')
            for entry in bucket:
                print(f'--> {entry}', end='')
            print()


def print_data(data):
    """Hàm hiển thị các entry/key/value của bảng băm."""
    for item in data:
        print(item)


if __name__ == '__main__':
    hash_table = HashTable(30)
    entries = [
        ("Hello", "Xin chào"), ("Love", "Yêu thương"), ("Baby", "Em bé"), ("Mother", "Mẹ"),
        ("Lovely", "Đáng yêu"), ("Ugly", "Xấu xí"), ("Chicken", "Con gà"), ("Kitty", "Mèo con"),
        ("Piggy", "Heo con"), ("Puppy", "Cún con"), ("Father", "Cha"), ("Computer", "Máy tính"),
        ("Smartphone", "Điện thoại thông minh"), ("Dictionary", "Từ điển"), ("Flower", "Bông hoa"),
        ("Fruit", "Trái cây"), ("Happy", "Sung sướng"), ("Banana", "Quả chuối"), ("Monkey", "Con khỉ"),
        ("Freeze", "Đóng băng")
    ]

    for key, value in entries:
        hash_table.insert(key, value)

    # hiển thị bảng băm
    print('==> Thông tin trong bảng băm: ')
    hash_table.display()

    print('==> Danh sách các key: ')
    print_data(hash_table.keys())

    print('==> Danh sách các value: ')
    print_data(hash_table.values())

    print('==> Danh sách các entry: ')
    print_data(hash_table.entries())
