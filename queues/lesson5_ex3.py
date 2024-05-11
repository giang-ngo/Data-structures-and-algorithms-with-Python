from collections import deque

queue = deque(maxlen=12)
queue.append('Loan')
queue.append('Phong')
queue.append('Nhân')
queue.appendleft('Linh')
queue.appendleft('Khánh')
queue.appendleft('Nhung')
queue.append('Bách')
queue.append('Hưng')

print(f'==> Số lượng phần tử trong hàng đợi: {len(queue)}')
print(f'==> Số lượng phần tử tối đa: {queue.maxlen}')
print('==> Các phần tử trong hàng đợi: ')
while len(queue) > 0:
    print(f'{queue.popleft()}')
