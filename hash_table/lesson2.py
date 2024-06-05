class Entry:
    """ Lớp biểu diễn một phần tử dữ liệu của bảng băm. """

    def __init__(self, key, value):
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
    def __init__(self, capacity=10):
        self.capacity = max(1, capacity)
        self.table = [[] for _ in range(self.capacity)]

    def hash_code(self, code):
        return code % self.capacity

    def insert(self, key, value):
        entry = Entry(key, value)
        index = self.hash_code(entry.hash)
        self.table[index].append(entry)

    def remove(self, key):
        """ Phương thức xóa bỏ phần tử có giá trị key khỏi bảng băm. """
        entry = Entry(key, None)
        index = self.hash_code(entry.hash)
        for i, item in enumerate(self.table[index]):
            if item.hash == entry.hash:
                self.table[index].pop(i)
                return True
        return False

    def display(self):
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
        ("Puppy", "Cún con"),
        ("Apple", "Quả táo"),
        ("Lemon", "Quả chanh")
    ]

    for key, value in entries:
        hash_table.insert(key, value)

    print('==> Thông tin trong bảng băm: ')
    hash_table.display()

    # tiến hành xóa
    hash_table.remove('Ok')
    hash_table.remove('Lemon')

    print('==> Bảng băm sau khi xóa một phần tử: ')
    hash_table.display()
