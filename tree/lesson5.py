import sys

class TreeNode:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None
        self.__height = 1  # Chiều cao của một node mới là 1

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
    def __init__(self):
        self.__root = None

    def insert(self, key):
        """ Phương thức chèn thêm node vào cây AVL """
        self.__root = self.__insert(self.__root, key)

    def __insert(self, root, key):
        """ Phương thức nội tại chèn node vào cây AVL. """
        if root is None:
            return TreeNode(key)

        if key < root.data:
            root.left = self.__insert(root.left, key)
        else:
            root.right = self.__insert(root.right, key)

        root.height = 1 + max(self.__get_height(root.left), self.__get_height(root.right))

        balance = self.__get_balance(root)

        # Trường hợp Left Left
        if balance > 1 and key < root.left.data:
            return self.__right_rotate(root)

        # Trường hợp Right Right
        if balance < -1 and key > root.right.data:
            return self.__left_rotate(root)

        # Trường hợp Left Right
        if balance > 1 and key > root.left.data:
            root.left = self.__left_rotate(root.left)
            return self.__right_rotate(root)

        # Trường hợp Right Left
        if balance < -1 and key < root.right.data:
            root.right = self.__right_rotate(root.right)
            return self.__left_rotate(root)

        return root

    def __left_rotate(self, z):
        """ Thực hiện quay trái trên cây con gốc là z. """
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.__get_height(z.left), self.__get_height(z.right))
        y.height = 1 + max(self.__get_height(y.left), self.__get_height(y.right))

        return y

    def __right_rotate(self, z):
        """ Thực hiện quay phải trên cây con gốc là z. """
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.__get_height(z.left), self.__get_height(z.right))
        y.height = 1 + max(self.__get_height(y.left), self.__get_height(y.right))

        return y

    def __get_height(self, root):
        """ Lấy chiều cao của cây có gốc là root. """
        if not root:
            return 0
        return root.height

    def __get_balance(self, root):
        """ Lấy hệ số cân bằng của cây có gốc là root. """
        if not root:
            return 0
        return self.__get_height(root.left) - self.__get_height(root.right)

    def print_helper(self):
        """ In cây theo cấu trúc. """
        self.__print_helper(self.__root, "", True)

    def __print_helper(self, root, indent, last):
        """ Phương thức trợ giúp để in cây theo cấu trúc. """
        if root:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(root.data)
            self.__print_helper(root.left, indent, False)
            self.__print_helper(root.right, indent, True)

if __name__ == '__main__':
    tree = AVLTree()
    nums = [33, 15, 52, 9, 21, 61, 8, 11, 16, 47, 5, 37, 1, 23, 12, 2]
    for num in nums:
        tree.insert(num)
    tree.print_helper()
