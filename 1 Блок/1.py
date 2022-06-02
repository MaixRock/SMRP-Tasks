def translate(text):
    global translated_text
    redLetter = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
                 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                 '.', ',', '-']
    for i in range(len(text) - 1):
        if redLetter.count(text[i]) == 0:
            translated_text = translated_text + text[i]
    translated_text = ' '.join(translated_text.split())
    print(translated_text)


translated_text = ''
translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
