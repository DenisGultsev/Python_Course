# def f(x):
#     return x ** 2


# print(f(4))  # 16
# print(type(f))  # <class 'function'>

# def f(x):
#     return x ** 2


# a = f
# print(a(4))  # 16
# print(type(a))  # <class 'function'>

# def calc1(x):
#     return x + x


# def calc2(x):
#     return x * x


# def math(op, x):
#     print(op(x))


# math(calc2, 5)

# def calk1(a, b):
#     return a * b


# def math(op, x, y):
#     print(op(x, y))


# math(lambda a, b: a + b, 5, 45)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data:
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)  # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

# data = '15 156 96 3 5 8 52 5'

# data = list(map(int, data.split()))
# print(data)

# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Функция filter

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)  # [0, 2, 4, 6, 8]

# filter() позволит избавиться от функции where, которую мы писали ранее

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Фуункция zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# print(data)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)  # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

# Функция enumerate

# users = ['Казань', 'Смоленск', 'Хабаровск', 'Москва']
# data = list(enumerate(users))

# print(data)
