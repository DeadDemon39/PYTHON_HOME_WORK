# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def recursia(num1, num2):
    if num2 == 0:
        return 1

    return num1 * recursia(num1, num2 - 1)


num = recursia(int(input('Введите число А: ')), int(input('Введите число В: ')))

print(f'Число А в степени В =  {num}')