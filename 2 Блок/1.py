def simple_map(transformation, values):
    list=[]
    for key in values:
        list.append(transformation(key))
    return list

list = [1, 3, 1, 5, 7]
print(*simple_map(lambda x:x+5, list))
