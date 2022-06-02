from functools import reduce

input = open('11.txt', 'r', encoding='utf-8').read()
data = [i.replace("/n", "") for i in map(str.strip, input)]
print(data)
