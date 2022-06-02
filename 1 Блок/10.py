def mirror(arr):
    mirrored_part = list(reversed(arr))
    arr += mirrored_part


arr = [1, 2]
mirror(arr)
print(*arr)
