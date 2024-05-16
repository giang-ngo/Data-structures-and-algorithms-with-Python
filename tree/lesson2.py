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

    def __pre_order(self, r):
        if r is not None:
            print(f'{r.data} ', end='')  # in ra giá trị node cha trước
            self.__pre_order(r.left)  # duyệt cây con trái
            self.__pre_order(r.right)  # duyệt cây con phải

    def in_order(self):
        self.__in_order(self.root)

    # phương thức duyệt in_order triển khai trong nội tại của BST
    def __in_order(self, r):
        if r is not None:
            self.__in_order(r.left)  # duyệt cây con trái
            print(f'{r.data} ', end='')  # in ra giá trị node cha
            self.__in_order(r.right)  # duyệt cây con phải

    def post_order(self):
        self.__post_order(self.root)

    def __post_order(self, r):
        if r is not None:
            self.__post_order(r.left)  # duyệt cây con trái
            self.__post_order(r.right)  # duyệt cây con phải
            print(f'{r.data} ', end='')  # in ra giá trị node cha


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
    print('==> Giá trị các node khi duyệt cây LNR: ')
    tree.in_order()
    print('\n==> Giá trị các node khi duyệt cây NLR: ')
    tree.pre_order()
    print('\n==> Giá trị các node khi duyệt cây LRN: ')
    tree.post_order()

#  hình ảnh cây nhị phân tìm kiếm trong ví dụ trên
# 	             __80__
# 	            /     \
#            50      100
#           /      /    \
#         30      90    120
#        / \       \    /  \
#       20  40     95 110  130
