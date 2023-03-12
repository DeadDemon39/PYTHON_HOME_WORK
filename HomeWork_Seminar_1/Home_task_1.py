# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input("Введите трехзначное число: ")

num1 = int(number[0])
num2 = int(number[1])
num3 = int(number[2])

sum = num1 + num2 + num3
print(sum)


