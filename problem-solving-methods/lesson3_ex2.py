# tìm số fibonacci thứ n
# fn = f(n-1) + f(n-2)

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = int(input('Enter a number: '))
    if n >= 0:
        result = fibonacci(n)
        print(f'F({n}) = {result}')
    else:
        print('Invalid input')