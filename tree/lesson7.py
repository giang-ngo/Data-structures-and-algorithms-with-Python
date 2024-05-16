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

    def get_height(self, root):
        if root is None:
            return 0
        left_child_height = self.get_height(root.left)
        right_child_height = self.get_height(root.right)
        return max(left_child_height, right_child_height) + 1

    def get_balance(self, root):
        """ Phương thức lấy hệ số cân bằng của một node. """
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

    def left_rotate(self, x):
        """ Phương thức xoay trái(RR) cây con """
        y = x.right
        left_y = y.left  # cây con trái của y
        y.left = x
        x.right = left_y  # gán x là node cha của cây con trái của y
        # cập nhật lại hệ số cân bằng của node x, y sau khi xoay
        x.height = self.get_height(x)
        y.height = self.get_height(y)
        return y

    def right_rotate(self, x):
        """ Phương thức xoay phải(LL) cây con. """
        y = x.left
        right_y = y.right
        y.right = x
        x.left = right_y
        x.height = self.get_height(x)
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
        # cập nhật hệ số cân bằng và tái cân bằng cây
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if key < root.left.data:  # TH xoay LL
                return self.right_rotate(root)
            else:  # TH xoay LR = RR + LL
                root.left = self.left_rotate(root.left)  # xoay RR
                return self.right_rotate(root)  # xoay LL
        if balance_factor < -1:
            if key > root.right.data:  # TH xoay RR
                return self.left_rotate(root)
            else:  # TH xoay RL = LL + RR
                root.right = self.right_rotate(root.right)  # xoay LL
                return self.left_rotate(root)  # xoay RR
        return root

    def remove(self, value):
        """ Phương thức xóa bỏ một node khỏi cây cân bằng. """
        self.__root = self.__remove(self.__root, value)

    def __remove(self, root, value):
        """ Phương thức nội tại xóa node khỏi cây AVL. """
        if root is None:  # nếu cây rỗng
            return root  # trả về None
        elif value < root.data:  # nếu node cần thêm nhỏ hơn node gốc
            root.left = self.__remove(root.left, value)  # xóa ở cây con trái
        elif value > root.data:  # nếu node cần thêm lớn hơn node gốc
            root.right = self.__remove(root.right, value)  # xóa ở cây con phải
        else:  # nếu tìm thấy node cần xóa
            if root.left is None:  # nếu node con trái của nó None
                return root.right  # cập nhật thành cây con phải
            elif root.right is None:  # nếu node con phải của nó None
                return root.left  # cập nhật thành cây con trái
            temp = self.min_node(root.right)  # tìm node giá trị min
            root.data = temp.data  # tráo đổi giá trị node min và node hiện tại
            root.right = self.__remove(root.right, temp.data)  # xóa bỏ node min

        if root is None:  # nếu root None thì kết thúc
            return root

        # cập nhật hệ số cân bằng cho node hiện thời
        root.height = self.get_height(root)
        # lấy hệ số cân bằng của node hiện thời
        balance_factor = self.get_balance(root)
        if balance_factor > 1:  # tiến hành các phép xoay phù hợp
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)  # xoay LL
            else:  # xoay LR
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)  # xoay RR
            else:  # xoay RL
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root  # trả về node hiện tại để update cây

    # Print the tree
    def print_helper(self):
        if self.__root is None:
            print('==> Cây rỗng. <==')
        else:
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
    # nums = [33, 15, 52, 9, 21, 61, 8, 11, 16, 47, 5, 37, 1, 23, 12, 2]
    nums = [33, 13, 53, 11, 21, 61, 8, 9]
    for num in nums:
        tree.insert(num)
    print('==> Cây AVL ban đầu: ')
    tree.print_helper()

    # xóa bỏ node có giá trị 13
    x = 13
    tree.remove(x)
    print(f'==> Cây AVL sau khi xóa node {x}: ')
    tree.print_helper()

    # xóa bỏ node có giá trị 13
    x = 33
    tree.remove(x)
    print(f'==> Cây AVL sau khi xóa node {x}: ')
    tree.print_helper()
'''
    Minh họa bằng hình ảnh:
    ==> Cây AVL ban đầu:
            ___33___
            /     |
           13      53
          / |      |
         9  21     61
        / |
       8  11
    ==> Sau khi xóa node 13:
            ___33___
            /     |
            9      53
          / |     | 
         8  21    61
             | 
            11
    ==> Sau khi xóa thêm node 33:
            ___21___
            /     |
           9      53
          / |      |
         8  11     61   
'''
