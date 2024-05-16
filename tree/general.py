class Node:
    """ Lớp mô tả thông tin một node. """

    def __init__(self, data=None):
        self.__data = data  # dữ liệu của node
        self.__child: list = []  # danh sách các node con của node hiện tại

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        self.__child.append(value)


class Tree:
    """ Lớp mô tả thông tin về cây tổng quát. """

    def __init__(self, data=None):
        """ Phương thức khởi tạo. Dùng để tạo một cây mới với node gốc
            có giá trị cho trước nếu data không None. Ngược lại nếu data None thì
            ta sẽ tạo một cây rỗng.
        """
        self.__root = None
        if data is not None:
            self.__root = Node(data)

    def insert(self, value, parent_value=None):
        """  Phương thức chèn node mới vào sau node có giá trị x. """
        self.__root = self.__insert(self.__root, value, parent_value)

    def __insert(self, parent_node, data, parent_value):
        """ Phương thức thêm node con mới vào node cha được chỉ định. """
        if parent_node is None:  # TH cây rỗng
            return Node(data)
        else:  # TH node đang xét khác None
            if parent_node.data == parent_value:  # nếu node đang xét chính là node cha
                parent_node.child.append(Node(data))  # bổ sung node con vào cho nó
            else:  # nếu node đang xét có các node con, tiếp tục đệ quy xét các node con
                number_of_child = len(parent_node.child)
                if number_of_child > 0:
                    for index in range(number_of_child):
                        self.__insert(parent_node.child[index], data, parent_value)
            return parent_node

    def traversal(self):
        """ Phương thức hiển thị các phần tử trên cây tổng quát. """
        self.__traversal(self.__root)

    def __traversal(self, r):
        """ Phương thức hiển thị nội tại của cây theo từng level. """
        if r is None:
            print('==> Cây rỗng! <==')
            return
        q = [r]  # tạo queue với phần tử gốc
        while len(q) > 0:
            n = len(q)
            while n > 0:
                p = q.pop(0)
                print(f'{p.data} ', end='')
                for i in range(len(p.child)):
                    q.append(p.child[i])
                n -= 1
            print()  # in xuống dòng


# hàm main
if __name__ == '__main__':
    tree = Tree(10)  # tạo cây với node gốc là 10
    tree.insert(20, 10)
    tree.insert(34, 10)
    tree.insert(56, 10)
    tree.insert(100, 10)
    tree.insert(77, 20)
    tree.insert(88, 20)
    tree.insert(111, 56)
    tree.insert(77, 100)
    tree.insert(85, 100)
    tree.insert(99, 100)
    tree.insert(510, 111)
    tree.insert(634, 99)
    tree.insert(241, 111)

    print('==> Các phần tử trong cây tổng quát: ')
    tree.traversal()

# mô tả cây:
'''
             _______10________
             /   /     |     |
            20  34     56    100
           / |         |    / | |
          77 88      111 77  85 99
                      / |         |
                    510 241      634
'''
