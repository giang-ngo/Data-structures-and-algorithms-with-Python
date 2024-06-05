class Entry:
    """ Lớp biểu diễn một phần tử dữ liệu của bảng băm. """

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.hash = self.hash_code()

    def hash_code(self):
        """ Phương thức băm tạo mã băm cho một key theo quy tắc:
            hash_value = s[0] * 31 ^ (n - 1) + s[1] * 31 ^ (n - 2) + ... + s[n - 1]
            Trong đó: s là chuỗi ký tự trong key, n là độ dài chuỗi đó và ^ là phép lũy thừa.
        """
        return sum(ord(c) * 31 ** (len(self.key) - 1 - i) for i, c in enumerate(self.key))

    def __str__(self):
        return f'[{self.key} - {self.value}]'


class HashTable:
    """ Lớp mô tả bảng băm. """

    def __init__(self, capacity=10):
        """ Hàm khởi tạo. """
        self.capacity = max(1, capacity)
        self.table = [[] for _ in range(self.capacity)]

    def hash_code(self, code):
        """ Phương thức trả về chỉ số của danh sách chứa phần tử với mã băm cho trước. """
        return code % self.capacity

    def insert(self, key, value):
        """ Phương thức chèn phần tử mới vào bảng băm """
        entry = Entry(key, value)
        index = self.hash_code(entry.hash)
        self.table[index].append(entry)

    def update(self, key, new_value):
        """ Phương thức cập nhật một phần tử nào đó trong bảng băm. """
        entry = Entry(key, new_value)
        index = self.hash_code(entry.hash)
        for element in self.table[index]:
            if element.hash == entry.hash:
                element.value = new_value
                return True
        return False

    def display(self):
        """ Phương thức hiển thị các phần tử trong bảng băm. """
        for i, bucket in enumerate(self.table):
            print(f'[{i}]: ', end='')
            for entry in bucket:
                print(f'--> {entry}', end=' ')
            print()


if __name__ == '__main__':
    hash_table = HashTable()
    entries = [
        ("Hello", "Xin chào"),
        ("Love", "Yêu thương"),
        ("Baby", "Em bé"),
        ("Mother", "Mẹ"),
        ("Lovely", "Đáng yêu"),
        ("Ugly", "Xấu xí"),
        ("Ok", "Tốt"),
        ("Chicken", "Con gà"),
        ("Kitty", "Mèo con"),
        ("Piggy", "Heo con"),
        ("Puppy", "Cún con")
    ]

    for key, value in entries:
        hash_table.insert(key, value)

    print('==> Thông tin trong bảng băm ban đầu: ')
    hash_table.display()

    # tiến hành cập nhật:
    hash_table.update("Hello", "XIN CHÀO")

    print('==> Thông tin trong bảng băm sau cập nhật: ')
    hash_table.display()
