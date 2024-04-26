import sys


class Entry:
    """ Lớp biểu diễn một phần tử dữ liệu của bảng băm. """

    def __init__(self, key, value=None):
        self.key: str = key
        self.value = value
        self.hash = self.hash_code()

    def hash_code(self):
        """ Phương thức băm tạo mã băm cho một key.
            Quy tắc băm: hash_value = s[0] * 31 ^ (n - 1) + s[1] * 31 ^ (n - 2) + ... + s[n - 1]
            Trong đó: s là chuỗi kí tự trong key, n là độ dài chuỗi đó và ^ là phép lũy thừa.
        """
        result = 0
        n = len(self.key)
        i = 1
        for c in self.key:
            result += ord(c) * pow(31, n - i)
            i += 1
        return result

    def __str__(self):
        return f'[{self.key} - {self.value}]'

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.hash == other.hash


class HashTable:
    """ Lớp mô tả bảng băm. """

    def __init__(self, capacity=10):
        """ Hàm khởi tạo. """
        if capacity <= 0:
            capacity = 10
        self.capacity = capacity
        # tạo một list của các list rỗng -> dạng table
        self.table: list = [[] for x in range(self.capacity)]
        self.MAX_SIZE = sys.maxsize - 8  # lấy giá trị tối đa có thể của bảng băm
        self._load_factor = 0.75
        self.__mod_count = 0
        self.__threshold = int(self.capacity * self._load_factor)
        self.__count = 0

    def hash_code(self, code):
        """ Phương thức trả về chỉ số của danh sách chứa phần tử với mã băm cho trước. """
        return code % self.capacity

    def insert(self, key, value):
        """ Phương thức chèn phần tử mới vào bảng băm """
        if self.__count >= self.__threshold:
            self.rehash()
        entry = Entry(key, value)
        index = self.hash_code(entry.hash)
        self.table[index].append(entry)
        self.__count += 1
        self.__mod_count += 1

    def update(self, key: str, new_value) -> bool:
        """ Phương thức cập nhật một phần tử nào đó trong bảng băm. """
        entry = Entry(key, new_value)
        index = self.hash_code(entry.hash)
        for element in self.table[index]:  # xét từng phần tử trong list tại vị trí index
            if element.hash == entry.hash:  # nếu tìm thấy phần tử cùng mã băm
                element.value = new_value  # cập nhật giá trị value của phần tử đó
                return True  # xác nhận cập nhật thành công
        return False  # xác nhận cập nhật thất bại

    def rehash(self):
        """ Phương thức băm lại bảng băm. """
        old_capacity = self.capacity
        old_table = self.table
        new_capacity = (old_capacity << 1) + 1
        if new_capacity - self.MAX_SIZE > 0:
            if old_capacity >= self.MAX_SIZE:
                return
            new_capacity = self.MAX_SIZE
        # thực hiện một số cập nhật
        new_table = [[] for x in range(new_capacity)]
        self.__mod_count += 1
        self.__threshold = min(int(new_capacity * self._load_factor), self.MAX_SIZE + 1)
        self.table = new_table
        self.capacity = new_capacity
        # copy các phần tử trong bảng băm cũ sang bảng băm mới
        for i in range(old_capacity):
            for element in old_table[i]:
                index = self.hash_code(element.hash)
                self.table[index].append(element)

    def keys(self):
        """ Phương thức lấy và trả về danh sách các khóa trong cặp key-value. """
        result = []
        for i in range(self.capacity):
            for item in self.table[i]:
                result.append(item.key)
        return result

    def values(self):
        """ Phương thức lấy và trả về danh sách các giá trị trong cặp key-value. """
        result = []
        for i in range(self.capacity):
            for item in self.table[i]:
                result.append(item.value)
        return result

    def entries(self):
        """ Phương thức lấy danh sách các entry của bảng băm. """
        result = []
        for i in range(self.capacity):
            for item in self.table[i]:
                result.append(item)
        return result

    def get(self, key):
        """ Phương thức trả về giá trị value ứng với key cho trước. """
        entry = Entry(key)
        search_index = self.hash_code(entry.hash)
        for element in self.table[search_index]:
            if element == entry:  # nếu phần tử entry đang xét là trùng khớp
                return element.value  # trả về đối tượng entry chứa thông tin đầy đủ
        return None

    def contains_key(self, key):
        """ Phương thức kiểm tra xem một key cho trước có tồn tại không. """
        entry = Entry(key)
        search_index = self.hash_code(entry.hash)
        for item in self.table[search_index]:
            if item == entry:
                return True
        return False

    def contains_value(self, value):
        """ Phương thức kiểm tra xem một value cho trước có tồn tại không. """
        for i in range(self.capacity):
            for item in self.table[i]:
                if item.value == value:
                    return True
        return False

    def display(self):
        """ Phương thức hiển thị các phần tử trong bảng băm. """
        for i in range(self.capacity):
            print(f'[{i}]: ', end='')
            for x in self.table[i]:
                print(f'--> {x}', end='')
            print()


def print_data(data):
    """ Hàm hiển thị các entry/key/value của bảng băm. """
    for item in data:
        print(item)


if __name__ == '__main__':
    hash_table = HashTable(25)
    hash_table.insert("Hello", "Xin chào")
    hash_table.insert('Love', 'Yêu thương')
    hash_table.insert('Baby', 'Em bé')
    hash_table.insert('Mother', 'Mẹ')
    hash_table.insert('Lovely', 'Đáng yêu')
    hash_table.insert('Ugly', 'Xấu xí')
    hash_table.insert('Chicken', 'Con gà')
    hash_table.insert('Kitty', 'Mèo con')
    hash_table.insert('Piggy', 'Heo con')
    hash_table.insert('Puppy', 'Cún con')
    hash_table.insert('Father', 'Cha')
    hash_table.insert('Flower', 'Bông hoa')
    hash_table.insert('Fruit', 'Trái cây')
    hash_table.insert('Happy', 'Sung sướng')
    hash_table.insert('Banana', 'Quả chuối')
    hash_table.insert('Monkey', 'Con khỉ')
    hash_table.insert('Freeze', 'Đóng băng')

    # hiển thị bảng băm
    print('==> Thông tin trong bảng băm: ')
    hash_table.display()

    print('==> Giá trị ứng với key "Kitty": ')
    print(hash_table.get('Kitty'))
    print('==> Giá trị ứng với key "Lovely": ')
    print(hash_table.get('Lovely'))

    print('==> Giá trị ứng với key "Quobee": ')
    print(hash_table.get('Quobee'))

    print('==> Giá trị ứng với key "Mommy": ')
    print(hash_table.get('Mommy'))

    # kiểm tra key có tồn tại không
    key_to_search = 'Hello'
    result = hash_table.contains_key(key_to_search)
    print(f'==> Key "{key_to_search}" có tồn tại trong bảng băm không? {result}')
    key_to_search = 'Good'
    result = hash_table.contains_key(key_to_search)
    print(f'==> Key "{key_to_search}" có tồn tại trong bảng băm không? {result}')

    # kiểm tra value có tồn tại không
    value_to_search = 'Con khỉ'
    result = hash_table.contains_value(value_to_search)
    print(f'==> Value "{value_to_search}" có tồn tại trong bảng băm không? {result}')
    value_to_search = 'Bla bla'
    result = hash_table.contains_value(value_to_search)
    print(f'==> Value "{value_to_search}" có tồn tại trong bảng băm không? {result}')
