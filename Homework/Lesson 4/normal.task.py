# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(list, n, m):
    """
    функция, возвращающая ряд Фибоначчи с n-элемента до m-элемента
    :param list: список
    :param n: n-элемент
    :param m: m-элемента
    :return: список
    """
    for i in range(len(list) - 2):
        list[i + 2] = list[i] + list[i + 1]
        if i == len(list):
            list.append(list[i + 2])
    c = list[n:m]
    return c
        #if i == len(list) когда i станет равным длине списка,то добавляем i + 2 в список
        #не знаю как это написать ;((((((


fibonacci([1, 1, 2, 3, 4, 5, 6, 7], 0, 8)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """
    функция, сортирующая принимаемый список по возрастанию (пузырьковый метод)
    :param origin_list: список
    :return: сортированный список
    """
    for i in range(0, len(origin_list) - 1):
        for el in range(0, len(origin_list) - 1):
            if origin_list[el] > origin_list[el + 1]:
                origin_list[el],origin_list[el + 1] = origin_list[el + 1],origin_list[el]

    return origin_list



    pass

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def search_h(string):
    """
    Ищет букву "о" в словах списка
    :param string: список
    :return: список
    """
    return 'o' in string

k = ['moskva', 'piter', 'morkov', 'carrot']

nl = [i for i in k if search_h(i)]
print(nl)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def properties_of_parallelograms ( A, B, C, D):
    """
    По четырем заданным точкам определяет параллелограмм это или нет
    :param A: точка
    :param B: точка
    :param C: точка
    :param D: точка
    :return: вывод да/нет
    """
    import math
    if math.sqrt((B[0] -A[0])**2 + (B[1] -A[1])**2) == math.sqrt((D[0] -C[0])**2 + (D[1] -C[1])**2) and math.sqrt((C[0] -B[0])**2 + (C[1] -B[1])**2) == math.sqrt((A[0] -D[0])**2 + (A[1] -D[1])**2):
        return 'Yes, this is f*n parallelogram!'
    return 'Sorry bro, but this is not parallelogram'



print(properties_of_parallelograms ( (-1, 1), (1, 7), (9, 3), (7, -3)))
print(properties_of_parallelograms ( (-1, 2), (1, 7), (9, 3), (7, -3)))