"""
    Дана некторая строка, содержащая какой-то текст и символы '[' - открывающей квадратной скобки
    и закрывающей квадратной скобки - ']'. Определить, валидная (корректная) ли данная строка.
    Валидной считается строка, в которой каждой открывающей скобке('[') соотвествуюет закрывающая (']').
    Например:
        some_string = "[array[0], [1, [[]], 3], []]" - валидная
        some_string = "[[]]" - валидная
        some_string = "][[[]]" - не валидная
        some_string = "[[[]]" - не валидная
        some_string = "[[][]]" - валидная
        some_string = "[[[[]" - не валидная
        some_string = "]]]]" - не валидная
        some_string = "]][]]" - не валидная
        some_string = "][" - не валидная
        some_string = "[[s][s][s[s]s]s]" - не валидная
    Задача: Напечатать в косоль True, если строка валидная и False, если не валидная. Прочие символы не учитываем.
    Подсказка: Для решения удобнее всего использовать цикл for, но вы можете предложить свой вариант решения.
"""
some_string = "[array[0], [1, [[]], 3], []]"

# TODO: код пишем здесь.
text = str(input ())
a = 0
b = 0
for i in text:
    if i == '[':
        a += 1
    if i == ']':
        b += 1
if b == a:
    print(f'{text} - валидная')
else:
    print(f'{text} - не валидная')


