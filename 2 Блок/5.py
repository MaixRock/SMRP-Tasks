def same_by(characteristic, objects):
    temp = characteristic(objects[0])
    for value in objects:
        current = characteristic(value)
        if (temp != current): return False
        temp = current
    return True

values = [2, 1, 1, 1]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('diff')
