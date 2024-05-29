import sys


class TreeNode:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None
        self.__height = 1

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

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value


class AVLTree:
    """ Lớp mô tả thông tin và thực hiện các thao tác trên cây AVL. """

    def __init__(self):
        self.__root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        """ Phương thức lấy hệ số cân bằng của một node. """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def pre_order(self):
        self.__pre_order(self.__root)

    def __pre_order(self, node):
        if not node:
            return
        print(f'{node.data} ', end='')
        self.__pre_order(node.left)
        self.__pre_order(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, key):
        """ Phương thức chèn thêm node vào cây AVL. """
        self.__root = self.__insert(self.__root, key)

    def __insert(self, node, key):
        """ Phương thức nội tại chèn node vào cây AVL. """
        if not node:
            return TreeNode(key)
        elif key < node.data:
            node.left = self.__insert(node.left, key)
        else:
            node.right = self.__insert(node.right, key)

        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1:
            if key < node.left.data:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if key > node.right.data:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def remove(self, key):
        """ Phương thức xóa bỏ một node khỏi cây cân bằng. """
        self.__root = self.__remove(self.__root, key)

    def __remove(self, node, key):
        """ Phương thức nội tại xóa node khỏi cây AVL. """
        if not node:
            return node

        if key < node.data:
            node.left = self.__remove(node.left, key)
        elif key > node.data:
            node.right = self.__remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.min_node(node.right)
            node.data = temp.data
            node.right = self.__remove(node.right, temp.data)

        if not node:
            return node

        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def print_helper(self):
        if not self.__root:
            print('==> Cây rỗng. <==')
        else:
            self.__print_helper(self.__root, '', True)

    def __print_helper(self, node, indent, last):
        if node:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("L--")
                indent += "   "
            else:
                sys.stdout.write("R--")
                indent += "|  "
            print(node.data)
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)


if __name__ == '__main__':
    tree = AVLTree()
    nums = [33, 13, 53, 11, 21, 61, 8, 9]
    for num in nums:
        tree.insert(num)
    print('==> Cây AVL ban đầu: ')
    tree.print_helper()

    # Xóa bỏ node có giá trị 13
    x = 13
    tree.remove(x)
    print(f'==> Cây AVL sau khi xóa node {x}: ')
    tree.print_helper()

    # Xóa bỏ node có giá trị 33
    x = 33
    tree.remove(x)
    print(f'==> Cây AVL sau khi xóa node {x}: ')
    tree.print_helper()
