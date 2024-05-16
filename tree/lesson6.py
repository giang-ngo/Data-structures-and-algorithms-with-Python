import sys


class TreeNode:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None
        self.__height = 0

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

    def get_height(self, root):
        if root is None:
            return 0
        left_child_height = self.get_height(root.left)
        right_child_height = self.get_height(root.right)
        return 1 + max(left_child_height, right_child_height)

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def min_node(self, root):
        if root is None or root.left is None:
            return root
        return self.min_node(root.left)

    def pre_order(self):
        self.__pre_order(self.__root)

    def __pre_order(self, root):
        if root is None:
            return
        print(f'{root.data} ', end='')
        self.__pre_order(root.left)
        self.__pre_order(root.right)

    def left_rotate(self, z):  # xoay RR
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = self.get_height(z)
        y.height = self.get_height(y)
        return y

    def right_rotate(self, z):  # xoay LL
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        z.height = self.get_height(z)
        y.height = self.get_height(y)
        return y

    def insert(self, key):
        """ Phương thức chèn thêm node vào cây AVL. """
        self.__root = self.__insert(self.__root, key)

    def __insert(self, root, key):
        """ Phương thức nội tại chèn node vào cây AVL. """
        if root is None:
            return TreeNode(key)
        elif key < root.data:
            root.left = self.__insert(root.left, key)
        else:
            root.right = self.__insert(root.right, key)
        root.height = self.get_height(root)
        # cập nhật nhân tố cân bằng và tái cân bằng cây
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if key < root.left.data:  # xoay LL
                return self.right_rotate(root)
            else:  # xoay LR
                root.left = self.left_rotate(root.left)  # RR
                return self.right_rotate(root)  # LL
        if balance_factor < -1:
            if key > root.right.data:  # xoay RR
                return self.left_rotate(root)
            else:  # xoay RL
                root.right = self.right_rotate(root.right)  # LL
                return self.left_rotate(root)  # RR
        return root

    # Print the tree
    def print_helper(self):
        self.__print_helper(self.__root, '', last=True)

    def __print_helper(self, root, indent, last):
        if root is not None:
            sys.stdout.write(indent)
            if root == self.__root:
                sys.stdout.write(indent)
            else:
                if last:
                    sys.stdout.write("L--")
                    indent += "   "
                else:
                    sys.stdout.write("R--")
                    indent += "|  "
            print(root.data)
            self.__print_helper(root.right, indent, False)
            self.__print_helper(root.left, indent, True)


if __name__ == '__main__':
    tree = AVLTree()
    nums = [33, 15, 52, 9, 21, 61, 8, 11, 16, 47, 5, 37, 1, 23, 12, 2]
    for num in nums:
        tree.insert(num)
    # in ra các node:
    tree.print_helper()

    # Minh họa trên hình vẽ biểu diễn:
    #               ___15___
    #              /        \
    #             9          33
    #           /   \       /   \
    #          5    11     21   52
    #         /\     \     /\   / \
    #        1  8    12  16 23 47  61
    #         \               /
    #          2             37
