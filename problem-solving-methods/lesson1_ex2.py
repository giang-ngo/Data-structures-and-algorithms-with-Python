if __name__ == '__main__':
    # number_array = [-1] * 5
    # number_array[0] = 0
    # number_array[4] = 5
    # # for item in number_array:
    # #     print(item)
    #
    # for index in range(-len(number_array), 0, 1):
    #     print(f'{index}: {number_array[index]}')

    friends = ['Alice', 'Bob', 'Carol', 'David', 'Eve']
    friends[3] = 'Mr.X'
    friends.sort(reverse=True)
    print(friends)
    # print(friends[:2])
    # print(friends[1:2])
    # print(friends[2:])
    # print(friends[-2:])
