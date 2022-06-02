arrey = []

while True:

    tmp = input()
    if tmp == '':
        break
    arrey += [tmp]

out = {}
for i in arrey:
    code = 0
    for j in i:
        code += ord(j.upper()) - ord('A') + 1
    out.update({i: code})

maxe = out[i]
put = {}
for hmmm in out:

    little = maxe + 1

    for i in out:
        if little > out[i]:
            little = out[i]
        if maxe < out[i]:
            maxe = out[i]

    assa = {"": 2*maxe}
    for i in out:
        if out[i] == little:
            assa.update({i: little})
            out[i] = maxe + 1

    del assa[""]
    while True:

        correct = True

        ass  = assa.copy()
        for i in assa:
            AAA = False
            for j in assa:
                if not AAA or i ==j:
                    AAA = i == j
                    continue
                for a in range(min([len(i), len(j)])):
                    if i[a].lower() < j[a].lower():
                        break
                    if i[a].lower() > j[a].lower():
                        correct = not correct
                        del ass[i]
                        ass.update({i: assa[i]})
                        break
        if correct:
            break

        assa  = ass.copy()

    put.update(ass)

for i in put:
    print(i)
