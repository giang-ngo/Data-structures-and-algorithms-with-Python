from collections import deque

stack = deque()  # tạo stack

# push các phần tử vào stack
stack.append('One')
stack.append('Two')
stack.append('Three')

# các phần tử trong stack theo thứ tự chèn vào
print('==> Các phần tử theo thứ tự chèn vào: ')
for item in stack:
    print(item)

# pop bỏ các phần tử theo thứ tự FILO
print('==> Các phần tử theo thứ tự bị pop bỏ: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())
