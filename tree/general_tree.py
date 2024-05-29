# ** tính ứng dụng ít, dừng lại ở mức tìm hiều cơ bản
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
        """ Thêm node con mới vào node cha được chỉ định. """
        if parent_node is None:
            return Node(data)

        if parent_node.data == parent_value:
            parent_node.child.append(Node(data))
        else:
            for child in parent_node.child:
                self.__insert(child, data, parent_value)

        return parent_node

    def traversal(self):
        """ Hiển thị các phần tử trên cây tổng quát. """
        if self.__root is None:
            print('==> Cây rỗng! <==')
        else:
            self.__traversal(self.__root)

    def __traversal(self, r):
        """ Hiển thị nội tại của cây theo từng level. """
        q = [r]  # tạo queue với phần tử gốc
        while q:
            level_nodes = []
            for _ in range(len(q)):
                node = q.pop(0)
                level_nodes.append(node.data)
                q.extend(node.child)
            print(" ".join(map(str, level_nodes)))  # in các phần tử trên cùng một level

    def display_tree(self):
        if self.__root is None:
            print("Empty Tree")
            return
        self.__display_tree(self.__root, "")

    def __display_tree(self, node, prefix):
        if node:
            print(prefix + "`- " + str(node.data))
            prefix += "   "
            for i, child in enumerate(node.child):
                is_last_child = (i == len(node.child) - 1)
                child_prefix = prefix if is_last_child else prefix + "|  "
                self.__display_tree(child, child_prefix)


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
    print('==> Hiển thị cây theo dạng cấu trúc: ')
    tree.display_tree()

# mô tả cây:
'''
             _______10________
             /   /     |     |
            20  34     56    100
           / |         |    / | |
          77 88      111  77  85 99
                    / |          |
                  510 241       634
'''
