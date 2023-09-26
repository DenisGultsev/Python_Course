# list_1 = []  # Создание пустого списка
# list_2 = list()  # Создание пустого списка
# list_1 = [7, 9, 11, 13, 15, 17]
# print(len(list_1))  # 6

# list_1 = []  # создание пустого списка
# for i in range(5):  # цикл выполнится 5 раз
#     n = int(input())  # пользователь вводит целое число
#     list_1.append(n)  # сохранение элемента в конец списка
# print(list_1)  # [12, 7, -1, 21, 0]

# list_1 = [12, 7, -1, 21, 0]
# for i in range(len(list_1)):
#     print(list_1[i])  # вывод каждого элемента списка

# list_1 = [12, 7, -1, 21, 0]
# for i in list_1:
#     print(i)  # вывод каждого элемента списка

# list_1 = [12, 7, -1, 21, 0]
# for i in range(len(list_1)):
#     print(list_1[i])

# Удаление последнего элемента списка.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop())  # 0
# print(list_1)  # [12, 7, -1, 21]
# print(list_1.pop())  # 21
# print(list_1)  # [12, 7, -1]
# print(list_1.pop())  # -1
# print(list_1)  # [12, 7]

# Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0))  # 12
# print(list_1)  # [7, -1, 21, 0]

# Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# list_1.insert(2, 11)
# print(list_1)  # [12, 7, 11, -1, 21, 0]

# Отрицательное число в индексе — счёт с конца списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])  # 1
# print(list_1[1])  # 2
# print(list_1[len(list_1)-1])  # 10
# print(list_1[-5])  # 6
# print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])  # [1, 2]
# print(list_1[len(list_1)-2:])  # [9, 10]
# print(list_1[2:9])  # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])  # []
# print(list_1[0:len(list_1):6])  # [1, 7]
# print(list_1[::6])  # [1, 7]

# Кортеж
# t = ()  # creating an empty tuple
# print(type(t))  # <class 'tuple'>

# t = (1,)
# print(type(t))

# t = (1,)
# print(type(t))

# t = (28, 9, 1990)
# print(type(t))

# colors = ['red', 'green', 'blue']
# print(colors)

# t = tuple(colors)
# print(t)

# print(t[0])
# print(t[2])

# for e in t:
#     print(e)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))  # r:red g:green b:blue

# Словари
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# # типы ключей могут отличаться
# print(dictionary['up'])  # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left'])  # ⇐
# # print(dictionary['type'])  # KeyError: 'type'
# del dictionary['left']  # удаление элемента
# for item in dictionary:  # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
#     # up: ↑
#     # down: ↓
#     # right: →

# Множества
# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}

# colors.add('red')
# print(colors)  # {'red', 'green', 'blue'}

# colors.add('gray')
# print(colors)  # {'red', 'green', 'blue', 'gray'}

# colors.remove('red')
# print(colors)  # {'green', 'blue', 'gray'}

# colors.discard('red')  # No error, 'red' is not present
# print(colors)  # {'green', 'blue', 'gray'}

# colors.clear()
# print(colors)  # set()

# Множества
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy()  # c = {1, 2, 3, 5, 8}

# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}

# i = a.intersection(b)  # i = {2, 5, 8}

# dl = a.difference(b)  # dl = {1, 3}

# dr = b.difference(a)  # dr = {13, 21}

# q = u.difference(i)  # q = {1, 21, 3, 13}

# print("Множество c:", c)
# print("Объединение множеств a и b:", u)
# print("Пересечение множеств a и b:", i)
# print("Разность множеств a и b:", dl)
# print("Разность множеств b и a:", dr)
# print("Симметрическая разность множеств a и b:", q)

# Неизменяемое или замороженное множество(frozenset)
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b)  # frozenset({1, 2, 3, 5, 8}

# list_1 = [exp for item in iterable]
# print(list_1)
# list_1 = [exp for item in iterable if conditional]
# print(list_1)

list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)  # [1, 2, 3, ..., 100]
