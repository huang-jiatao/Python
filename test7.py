import os

'''
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def main():
    print(power(5, 3))


if __name__ == '__main__':
    main()
'''
# ���õݹ麯������׳�
# N! = 1 * 2 * 3 * ... * N

print('�׳�����')
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

# ���õݹ麯���ƶ���ŵ��:

print('��ŵ������')
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')
