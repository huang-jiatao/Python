import os


def test():
    print('list lience')
    L = [0, 1, 2, 3, 4, 5, 6, 7]
    print(L)
    for i in range(8):
        L.append(i)
    print(L)
    print(L[0], L[4::3])
    s = '�Ͼ��ƾ���ѧ'
    print(type(s))
    print(s[0:-1:2])


def main(*args, **kw):
    test()


if __name__ == '__main__':
    main()
