# lớp mô tả thông tin của một sinh viên
class Student:
    def __init__(self, student_id=None, first_name=None, last_name=None, gpa=0.0):
        self.__gpa: float = gpa
        self.__last_name: str = last_name
        self.__first_name: str = first_name
        self.__student_id: str = student_id

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    def __str__(self):
        return f'[{self.student_id}, {self.first_name}, {self.last_name}, {self.gpa}]'

    def __eq__(self, other):  # phương thức chỉ định sự tương đương của hai SV
        if other is None:
            return False
        else:
            return self.student_id == other.student_id  # cùng mã SV