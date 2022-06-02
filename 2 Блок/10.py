import itertools

dictio = input().lower().split(" ")
message = input().lower().split(" ")
out_put_massage = ""

for i in message:
    right = False
    tmp = list(itertools.permutations(i))
    for j in dictio:
        if len(i) != len(j):
            continue

        tmp2 = list(itertools.permutations(j))
        for var in tmp:
            right = var in tmp2 and i != j
        if right:
            break
    if right:
        out_put_massage += '#' * len(i) + ' '
        continue
    else:
        out_put_massage += str(i) + ' '

print(out_put_massage)
