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

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)  # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
print(res)
