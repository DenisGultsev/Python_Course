
# n = 5
# print(type(n))

# n = 'fddf'
# print(type(n))

# n = 'fd\'df'
# print(n)

# n = 'fd"gbgfb"df'
# print(n)


# a = 5
# b = 5.89
# c = 'hello'

# print(a, b, c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))

# print('Введите первое число: ')
# a = input()
# b = input('Введите второе число: ')

# print(a, ' + ', b, ' = ', a + b)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c)
# print(type(c))

# c = 5.89
# print(c + '56')
# print(type(c))
# c = str(c)
# print(c + '89')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# v = 'fvdfv'
# v = int(v)

# print('Введите первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))

# name = input("Введите ваше имя: ")  # Запрашивает у пользователя ввод имени
# print("Привет, ", name)             # Выводит приветствие с введенным именем

# name = "John"
# age = 25
# print(f"My name is {name} and I am {age} years old.")

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ!')
# else:
#     print('Привет, ' + username)

# x = 3.14159
# rounded = round(x, 2)
# print(rounded)  # Выведет 3

# a = 1 < 3 < 8 < 10
# print(a)

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)  # 9

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит')
# print(i)

# Метод флажка

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:  # если остаток при делении чисел n на i равен 0
        flag = False
        print(i)
    elif i > n // 2:  # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1
