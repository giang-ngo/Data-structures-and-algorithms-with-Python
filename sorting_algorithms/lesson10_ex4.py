import tensorflow as tf

if __name__ == '__main__':
    arr = [1.25, 3.66, 0.36, 1.14, 8.21, 3.85, 7.54, 6.29, 4.23, 5.17]
    print('==> Trước khi sắp xếp: ')
    print(arr)
    print('==> Sau khi sắp xếp: ')
    result = tf.sort(arr)
    print(result.numpy())