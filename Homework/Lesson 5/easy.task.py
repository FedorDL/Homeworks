# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

l = [1, 2, 4, 0]
l2 = [i*i for i in l]
print(l2)

print('\n')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits1 = ['apple', 'pineapple', 'banana']
fruits2 = ['banana', 'peach', 'apple']
fruits5 = []
fruits4 = [fruits5.append(i) for i in (fruits2 + fruits1) if i not in fruits5 and (fruits2 + fruits1).count(i) > 1]
print(fruits5)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list1 = [3, 12, 4,-3, 0, 15, -15]
list2 = [i for i in list1 if i % 3 == 0 and i > 0 and i % 4 != 0]
print(list2)