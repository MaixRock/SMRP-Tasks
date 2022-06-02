def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


matrix = [[1, 2], [3, 4]]
for line in transpose(matrix):
    print(*line)
