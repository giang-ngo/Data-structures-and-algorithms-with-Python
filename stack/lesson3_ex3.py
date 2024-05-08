from queue import LifoQueue

stack = LifoQueue()  # tạo stack

# chèn các phần tử vào stack
stack.put('one')
stack.put('two')
stack.put('three')

# pop bỏ các phần tử
print('==> Các phần tử theo thứ tự bị pop bỏ: ')
print(stack.get())
print(stack.get())
print(stack.get())
