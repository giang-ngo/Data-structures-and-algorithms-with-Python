from queue import Queue

q = Queue(10)

for item in range(10, 110, 10):
    q.put(item)

print(f'==> Số phần tử trong hàng đợi: {q.qsize()}')
print('==> Các phần tử trong hàng đợi: ')
while not q.empty():
    print(q.get())

print('==> Sau khi đã xóa hết các phần tử trong hàng đợi: ')
print(f'==> Số phần tử trong hàng đợi: {q.qsize()}')
