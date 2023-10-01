# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)


# sumNumbers(5)


# def sum_numbers(n, y='Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa


# a = sum_numbers(5, 'qwert')
# print(a)

# def sum_str(*args):
#     res = ' '
#     for i in args:
#         res += i
#     return res


# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r', 'f'))
# print(sum_str(1, 8, 9))

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa


# n = int(input())  # 5
# print(sumNumbers(n))  # 15

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     return  # выход из функции

# s = "Hello"
# n = 3
# result = s * n
# print(result)

# def new_string(symbol, count=3):
#     return symbol * count


# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # !!!
# print(new_string(4))  # 12

# def concatenatio(*params):
#     res = ""
#     for item in params:
#         res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1'))  # a1
# print(concatenatio(1, 2, 3, 4))  # TypeError: ...

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)


# list_1 = []
# for i in range(1, 11):
#     list_1.append(fib(i))
# print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)


# print(quicksort([10, 5, 2, 3]))

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1


# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)

# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return sum(a + 1, b - 1)


# a = 3
# b = 5
# print(sum(a, b))
