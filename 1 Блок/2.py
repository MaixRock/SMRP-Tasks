import math


def discriminant(a, b, c):
    dis = b**2 - 4 * a * c
    if dis < 0:
        print("Дискриминант меньше 0")
        return -1
    return dis


def larger_root(p, q):
    dis = discriminant(1, p, q)
    if dis < 0:
        print("Дискриминант меньше 0")
        return 0
    x1 = (-p + math.sqrt(dis)) / 2
    x2 = (-p - math.sqrt(dis)) / 2
    if x1 > x2:
        return x1
    else:
        return x2


def smallest_root(p, q):
    dis = discriminant(1, p, q)
    if dis < 0:
        print("Дискриминант меньше 0")
        return 0
    x1 = (-p + math.sqrt(dis)) / 2
    x2 = (-p - math.sqrt(dis)) / 2
    if x1 < x2:
        return x1
    else:
        return x2




print("Введите p")
p = int(input())

print("Введите q")
q = int(input())

print(discriminant(1, p, q))
print(larger_root(p, q), " ", smallest_root(p, q))