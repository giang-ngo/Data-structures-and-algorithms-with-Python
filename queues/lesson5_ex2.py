from queue import PriorityQueue

q = PriorityQueue(10)

for item in range(1000, 0, -100):
    q.put(item)

print(f'==> Số phần tử trong hàng đợi: {q.qsize()}')
print('==> Các phần tử trong hàng đợi: ')
while not q.empty():
    print(q.get())

print('==> Sau khi đã xóa hết các phần tử trong hàng đợi: ')
print(f'==> Số phần tử trong hàng đợi: {q.qsize()}')
