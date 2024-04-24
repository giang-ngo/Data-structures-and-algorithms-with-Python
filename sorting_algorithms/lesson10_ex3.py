import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({
        'student_id': ['SV1001', 'SV1002', 'SV1003', 'SV1004', 'SV1005', 'SV1006', 'SV1007'],
        'first_name': ['Nam', 'Hoa', 'Bách', 'Trung', 'Loan', 'Mai', 'Anh'],
        'last_name': ['Hoàng', 'Lương', 'Ngô', 'Trần', 'Lê', 'Nguyễn', 'Triệu'],
        'gpa': [3.26, 3.36, 3.21, 3.54, 3.04, 3.87, 3.41]
    })

    # trước khi sắp xếp:
    print(df)

    # sắp xếp theo cột gpa:
    df.sort_values(by=['gpa'], inplace=True)  # theo một tiêu chí
    print('==> Sau khi sắp xếp theo cột gpa: ')
    print(df)
