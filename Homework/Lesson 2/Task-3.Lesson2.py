# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

num = int(input("Введите число: "))
x = num%10
num = num//10
while num > 0:
    if num%10 > x:
        x = num%10
    num = num//10
print('Максимальная цифра в данном числе равна', x)

#Решение через if
number = int(input("Введите число: "))
number = str(number)
if number.find("9") >= 0:
    print ("Максимальная цифра в данном числе равна 9")
elif number.find("8") >= 0:
    print("Максимальная цифра в данном числе равна 8")
elif number.find("7") >= 0:
    print("Максимальная цифра в данном числе равна 7")
elif number.find("6") >= 0:
    print("Максимальная цифра в данном числе равна 6")
elif number.find("5") >= 0:
    print("Максимальная цифра в данном числе равна 5")
elif number.find("4") >= 0:
    print("Максимальная цифра в данном числе равна 4")
elif number.find("3") >= 0:
    print("Максимальная цифра в данном числе равна 3")
elif number.find("2") >= 0:
    print("Максимальная цифра в данном числе равна 2")
elif number.find("1") >= 0:
    print("Максимальная цифра в данном числе равна 1")

#Решение через for не доделал, не могу понять как сохранить максимальное значение в переменной
num = int(input("Введите число: "))
s = str(num)
n = len(s)
for i in range(n - 1):
    if int(s[i]) > int(s[i + 1]):
        a = int(s[i])
        #print(a, end=' ')
    else:
        b = int(s[i + 1])
        #print(b)
        if b > a:


