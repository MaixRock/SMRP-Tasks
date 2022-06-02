square = [map(lambda x: int(x),(input().split(" "))) for i in range(3)]
a = [list(i) for i in square]
for i in list(zip(a)):
    a += [i[0]]
if all([not bool(sum(i) - sum(a[0])) for i in a]):
    print("YES")
else:
    print("NO")
