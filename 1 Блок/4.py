items = []
cost = []
a = 1


def add_item(item_Name, item_Cost):
    items.append(item_Name)
    cost.append(int(item_Cost))


def print_receipt():
    if not items:
        return
    if len(items) > 0:
        global a
        print('Чек ', a, '. Всего предметов: ', len(items), sep='')
        b = 0
    for i in range(len(items)):
        print(items[i], '-', cost[b])
        b += 1
    print('Итого:', sum(cost))
    print('-----')
    items.clear()
    cost.clear()
    a += 1



add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
