verse = input("Где стихи Винни?\n").split(" ")

rythm = []
for line in verse:
    for letter in line:
        rythm += [len([letter for letter in line if letter in 'уеыаоэяию'])]

for i in rythm:
    if rythm[0] != rythm[i]:
        print("Пам парам")

print("Парам пам-пам")
