Text = open('7.txt', 'r', encoding='utf-8')

dictonary = []
for i, val in enumerate(Text, start=1):
    lst = val.replace('.', '').split()
    for word in lst:
        dictonary.append(word)

for i, word in enumerate(dictonary, start=1):
    if word.istitle():
        print(f' {i} - {word}')

