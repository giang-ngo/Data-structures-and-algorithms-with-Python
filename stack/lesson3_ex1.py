# tạo stack
stack = []

# push phần tử vào stack:
stack.append('One')
stack.append('Two')
stack.append('Three')

# in ra các phần tử trong stack:
print('==> Các phần tử trong stack: ')
for item in stack:
    print(f'{item}')

# pop các phần tử khỏi stack
print('==> Thứ tự các phần tử trong stack khi pop:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
