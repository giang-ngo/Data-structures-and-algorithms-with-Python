# tính n!
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * (4 * 3 * 2 * 1)
# 5! = 5 * 4!
# 5! = 5 * 4 * 3!
# 5! = 5 * 4 * 3 * 2!
# 5! = 5 * 4 * 3 * 2 * 1!

# n! = n * (n - 1)!

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    for x in range(11):
        result = factorial(x)
        print(f'{x}! = {result}')
