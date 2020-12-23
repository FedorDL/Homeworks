# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
def convert(km):
    """
    Переводит километры в мили
    :param km: введите количество километров для перевода в мили
    :return:None
    """
    miles = km * 1.609
    print(miles)


convert(20)

print('\n')


# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    """
    Округляет полученное произвольное десятичное число до кол-ва знаков
     (кол-во знаков передается вторым аргументом).Округление должно
     происходить по математическим правилам (0.6 --> 1, 0.4 --> 0)
    :param number: полученное произвольное десятичное число
    :param ndigits: кол-во знаков
    :return:
    """
    lnumber = number * 10 ** ndigits
    rnumber = lnumber // 1
    rnumber = int(rnumber)
    a = str(rnumber)
    c =[]
    d =[]
    for i in a:
        if int(i) > 6:
            c.append(int(i) + 1)
        else:
            c.append(int(i))
    for u in c:
        if int(u) < 9:
            d.append(int(u))
        else:
            d.append(1)
        print(d)
    #e = ''.join(map(str,d))
   #f = int(e) / 10 ** ndigits
    #print(f)

    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

print('\n')
# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    """
    Сравнивает сумму трех первых и последних цифр
    :param ticket_number: число
    :return: True False
    """
    ticket_number = str(ticket_number)
    a = ticket_number[:3]
    b = ticket_number[3:]
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        sum1 += int(a[i])
    for u in range(len(b)):
        sum2 += int(b[u])
    if sum1 == sum2:
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
