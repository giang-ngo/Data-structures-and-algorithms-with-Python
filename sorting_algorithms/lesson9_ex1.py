import numpy as np

from sorting_algorithms.student import Student


def show_result(students: np.array):
    for student in students:
        print(student)


def test():
    students = [
        Student("SV1001", "Nam", "Hoàng", 3.26),
        Student("SV1002", "Hoa", "Lương", 3.36),
        Student("SV1003", "Bách", "Ngô", 3.21),
        Student("SV1004", "Trung", "Trần", 3.54),
        Student("SV1005", "Loan", "Lê", 3.04),
        Student("SV1006", "Mai", "Nguyễn", 3.87)
    ]
    print('==> Trước khi sắp xếp: ')
    show_result(students)

    # cách 1: dùng list.sort()
    # tiến hành sắp xếp theo điểm gpa
    students.sort(key=lambda student: -student.gpa)
    # students.sort(key=lambda student: student.gpa, reverse=True)
    print('==> Sau khi sắp xếp giảm dần theo điểm gpa: ')
    show_result(students)

    # cách 2: dùng hàm sorted()
    # tiến hành sắp xếp theo tên
    sorted_students = sorted(students, key=lambda s: s.first_name, reverse=True)
    print('==> Sau khi sắp xếp giảm dần theo tên z-a: ')
    show_result(sorted_students)


if __name__ == '__main__':
    test()
