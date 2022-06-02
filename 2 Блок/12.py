import math
import functools

a = int(input())
arrey = []
while True:

    b = input()
    if b == '':
        break

    arrey += [int(b)]


print(functools.reduce(math.gcd,arrey))
