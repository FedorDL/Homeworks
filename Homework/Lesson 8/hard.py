from random import randint

import numpy


def touch_line():
    a = numpy.zeros(9, dtype=int)
    b = sorted(numpy.random.choice(9, 5, False))
    c = sorted(numpy.random.choice(91, 9, False))
    for i in b:
            a[i] = c[i]
    return a

def touch_card(*args):
    return numpy.vstack([*args])

human_card = touch_card(touch_line(),touch_line(),touch_line())

r_number = randint(1, 91)
print(r_number)
print(human_card)
for i in range(len(human_card[0])):
        if human_card[0][i] == r_number:
                human_card[0][i] = 0
for i in range(len(human_card[1])):
        if human_card[1][i] == r_number:
                human_card[1][i] = 0
for i in range(len(human_card[2])):
        if human_card[2][i] == r_number:
                human_card[2][i] = 0
print(human_card)

# k = touch_line()
# l = touch_line()
# m = touch_line()
# print(k, '\n', l, '\n', m, '\n')
# # print(human_card)
# #

# def search_values(*args):
#         k = touch_line()
#         l = touch_line()
#         m = touch_line()
#         print(k, '\n', l, '\n', m, '\n')
#         r_number = randint(1, 91)
#         print(r_number)
#         for i in range(len(k)):
#             if k[i] == r_number:
#                 print(True)
#                 k[i] = 0
#
#         for u in range(len(l)):
#             if l[u] == r_number:
#                 print(True)
#                 l[u] = 0
#
#         for y in range(len(k)):
#             if m[y] == r_number:
#                 print(True)
#                 m[y] = 0
#         print(k, '\n', l, '\n', m, '\n')
#
# print(search_values())



