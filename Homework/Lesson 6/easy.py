# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5

try:
    a = float(input("a = "))
    b = float(input("b = "))
    if a < 0 or b < 0:
        raise ValueError('Вы ввели отрицательное число...Попробуйте снова')
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError:
    print('Вы ввели не число (отрицательное число)...Попробуйте снова')

# В данной программе ошибка (нельзя получить среднее геометрическое из отрицательного числа),
# но она не появляется т.к. корень из чисел получается возведением в степень в 0.5.
# Если использовать math.sqrt то ошибка появится.

print('\n')

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os, shutil, sys

dir = [('dir_' + str(i+1)) for i in range(9)]

def makedirs(paths):
    path_dir = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(path_dir)
    except FileExistsError:
        print("Невозможно создать файл, так как он уже существует")

for i in dir:
    makedirs(i)

def deletedirs(name_dirs):
    try:
        path_dir = os.path.join(os.getcwd(), name_dirs)
        os.removedirs(path_dir)
    except Exception:
        print('Невозможно удалить...Попробуйте еще')

for i in dir:
    deletedirs(i)

print('\n')
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

def search_dir(name):
    try:
        for i in os.listdir(name):
            print(i)
    except Exception:
        print('Невозможно найти...Попробуйте еще')

name = os.getcwd()
print(search_dir(name))

print('\n')
# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(first_file, backup_file):
    try:
        shutil.copy(first_file, backup_file)
    except Exception:
        print('Невозможно копировать...Попробуйте еще')
