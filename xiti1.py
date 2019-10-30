import os


def fun(name):
    name = name[0].upper() + name[1:].lower()
    return name


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(fun, L1))
print(L2)
