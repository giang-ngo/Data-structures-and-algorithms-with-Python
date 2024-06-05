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
        result = 0
        for i, c in enumerate(self.key):
            result += ord(c) * (31 ** (len(self.key) - 1 - i))
        return result

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

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f'[{i}]: ', end='')
            for entry in bucket:
                print(f'--> {entry}', end=' ')
            print()


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.insert("Hello", "Xin chào")
    hash_table.insert('Love', 'Yêu thương')
    hash_table.insert('Baby', 'Em bé')
    hash_table.insert('Mother', 'Mẹ')
    hash_table.insert('Lovely', 'Đáng yêu')
    hash_table.insert('Ugly', 'Xấu xí')
    hash_table.insert('Ok', 'Tốt')
    hash_table.insert('Chicken', 'Con gà')
    hash_table.insert('Kitty', 'Mèo con')
    hash_table.insert('Piggy', 'Heo con')
    hash_table.insert('Puppy', 'Cún con')

    print('==> Thông tin trong bảng băm: ')
    hash_table.display()
