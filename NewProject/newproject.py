def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        mid1 = nums[n // 2]
        mid2 = nums[n // 2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = nums[n // 2]
    return median


# Пример использования функции
numbers = [5, 3, 1, 2, 4]
median = find_median(numbers)
print("Медиана:", median)
