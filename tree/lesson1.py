# lớp mô tả thông tin về một node của cây nhị phân tìm kiếm
class Node:
    def __init__(self, data=None):
        self.__left = None
        self.__right = None
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class BinarySearchTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        self.__root = value

    def add(self, value):
        self.__root = self.__add(self.__root, value)

    def __add(self, node, value):
        if node is None:
            return Node(value)
        if value >= node.data:
            node.right = self.__add(node.right, value)
        else:
            node.left = self.__add(node.left, value)
        return node

    def in_order(self):
        self.__in_order(self.__root)
        print()

    def __in_order(self, node):
        if node:
            self.__in_order(node.left)
            print(f'{node.data} ', end='')
            self.__in_order(node.right)

    def display_tree(self):
        if self.__root is None:
            print("Empty Tree")
            return
        self.__display_tree(self.__root, 0, False, "")

    def __display_tree(self, node, level, is_last, prefix):
        if node is not None:
            print(prefix, "`- " if is_last else "|- ", node.data, sep="")
            prefix += "   " if is_last else "|  "
            child_count = (node.left is not None) + (node.right is not None)
            if node.left:
                self.__display_tree(node.left, level + 1, child_count == 1, prefix)
            if node.right:
                self.__display_tree(node.right, level + 1, True, prefix)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(80)
    tree.add(50)
    tree.add(100)
    tree.add(30)
    tree.add(40)
    tree.add(20)
    tree.add(90)
    tree.add(120)
    tree.add(95)
    tree.add(130)
    tree.add(110)

    print('==> Giá trị các node trong cây: ')
    tree.in_order()
    print('\nCấu trúc cây nhị phân:')
    tree.display_tree()

#  hình ảnh cây nhị phân tìm kiếm trong ví dụ trên
# 		        __80__
# 	           /     \
#            50      100
#           /      /    \
#         30      90    120
#        / \       \    /  \
#       20  40     95 110  130
