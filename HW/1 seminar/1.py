'''
Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''

def sum_nums(nums):
    if len(nums) != 3:
        print("Только три цифры :) ")
    else:
        lst_nums = []
        for digit in range(len(nums)):
            lst_nums.append(int(nums[digit]))
        result = sum(lst_nums)
        print(f'{result} ({nums[0]} + {nums[1]} + {nums[2]})')
        return result

nums = input("Введите три числа без пробелов: ")
result = sum_nums(nums)
