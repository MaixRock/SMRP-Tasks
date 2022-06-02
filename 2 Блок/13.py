from math import ceil

Data=[]
input = open('13.txt', 'r', encoding='utf-8').read()
cities = input.split("\n")

popul = {}

for x in cities:
    city, _, pop = x.split()
    pop = int(ceil(int(pop) / 100000)) * 100
    popul[pop] = popul.get(pop, []) + [city]

popul = sorted(popul.items())

for k, v in popul:
    print(int(k) - 100, '-', k, ':', ",".join(sorted(v)))



