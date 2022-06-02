from itertools import product
suits = ['пик', 'треф', 'бубен', 'червей']
nominals = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
inputsuit = input()
suits.remove(inputsuit)
for n, s in product(nominals, suits):
    print(n, s)