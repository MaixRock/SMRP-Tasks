name = ''


def polite_input(question):
    global name
    if name == '':
        nam = input('Как вас зовут?' + '\n')
        name = nam
    q_in = str(name) + ', ' + str(question) + '\n'
    conversation = input(q_in)
    return conversation


age = polite_input('укажите возраст')
school_number = polite_input('укажите номер школы')
class_num = polite_input('укажите полный номер класса')
