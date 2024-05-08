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
        self.root = self.__add(self.__root, value)

    # phương thức add triển khai trong nội tại của BST
    def __add(self, r, value) -> Node:
        if r is None:  # nếu node r đang xét là None
            return Node(value)  # tạo và trả về node mới
        else:  # nếu r không None, tiếp tục xét
            if value > r.data:  # nếu giá trị cần thêm vào cây lớn hơn node đang xét
                r.right = self.__add(r.right, value)  # tiến hành chèn vào bên phải
            else:  # ngược lại
                r.left = self.__add(r.left, value)  # chèn bên trái node hiện thời
            return r  # chèn node mới xong thì return để update cây

    def pre_order(self):
        self.__pre_order(self.root)
        print()

    def __pre_order(self, r):
        if r is not None:
            print(f'{r.data} ', end='')  # in ra giá trị node cha trước
            self.__pre_order(r.left)  # duyệt cây con trái
            self.__pre_order(r.right)  # duyệt cây con phải

    def in_order(self):
        self.__in_order(self.root)
        print()

    # phương thức duyệt in_order triển khai trong nội tại của BST
    def __in_order(self, r):
        if r is not None:
            self.__in_order(r.left)  # duyệt cây con trái
            print(f'{r.data} ', end='')  # in ra giá trị node cha
            self.__in_order(r.right)  # duyệt cây con phải

    def post_order(self):
        self.__post_order(self.root)
        print()

    def __post_order(self, r):
        if r is not None:
            self.__post_order(r.left)  # duyệt cây con trái
            self.__post_order(r.right)  # duyệt cây con phải
            print(f'{r.data} ', end='')  # in ra giá trị node cha

    def count_node(self):
        """ Đếm số node có trong cây. """
        return self.__count_node(self.root)

    def __count_node(self, r):
        """ Phương thức nội tại đếm số node hiện có trong cây BST. """
        if r is None:
            return 0
        else:
            return 1 + self.__count_node(r.left) + self.__count_node(r.right)

    def count_leaf_node(self):
        """ Đếm số lượng node lá trên cây. """
        return self.__count_leaf_node(self.root)

    def __count_leaf_node(self, r):
        """ Phương thức nội tại đếm số lượng node lá trên cây. """
        if r is None:
            return 0
        # node lá là node có cây con trái và phải đều None
        if r.left is None and r.right is None:
            return 1
        return self.__count_leaf_node(r.left) + self.__count_leaf_node(r.right)

    def __min_node(self, r):
        """ Phương thức nội tại tìm và trả về node nhỏ nhất của cây con bên phải. """
        while r.left is not None:
            r = r.left
        return r.data

    def remove(self, value):
        """ Phương thức xóa node khỏi cây. """
        self.root = self.__remove(self.root, value)

    def __remove(self, r, x):
        """ Phương thức nội tại xóa node có giá trị x khỏi cây. """
        if r is None:
            print(f'==> Không tồn tại node có giá trị {x}.')
            return None
        if x < r.data:
            r.left = self.__remove(r.left, x)
        elif x > r.data:
            r.right = self.__remove(r.right, x)
        else:
            if r.left is None:
                r = r.right
            elif r.right is None:
                r = r.right
            else:
                r.data = self.__min_node(r.right)
                r.right = self.__remove(r.right, r.data)
        return r  # trả về node r để cập nhật cây

    def search(self, key):
        """ Phương thức tìm kiếm theo từ khóa cần thiết. """
        return self.__search(self.root, key)

    def __search(self, r: Node, key):
        """ Phương thức tìm kiếm nội tại trong lớp BST. """
        if r is None:  # nếu node đang xét là None
            return None  # không có kết quả tìm kiếm
        if r.data == key:  # nếu tìm thấy
            return r.data  # trả về giá trị node cần tìm
        if key < r.data:  # nếu node cần tìm nhỏ hơn node hiện tại
            return self.__search(r.left, key)  # tìm bên cây con trái của nó
        else:  # ngược lại, nếu node cần tìm lớn hơn node hiện tại
            return self.__search(r.right, key)  # tìm ở cây con bên phải


def search_result(tree: BinarySearchTree, key):
    result = tree.search(key)
    if result is not None:
        print(f'==> Tìm thấy node có giá trị {key}')
    else:
        print(f'==> Không tìm thấy node có giá trị {key}')


def test():
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
    print('==> Giá trị các node khi duyệt cây LNR: ')
    tree.in_order()

    # tìm kiếm một số node trên cây nhị phân tìm kiếm
    search_result(tree, 20)
    search_result(tree, 120)
    search_result(tree, 200)


if __name__ == '__main__':
    test()

#  hình ảnh cây nhị phân tìm kiếm trong ví dụ trên
# 	        __80__
#   	       /     \
#            50      100
#           /      /    \
#         30      90    120
#        / \       \    /  \
#       20  40     95 110  130
