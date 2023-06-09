# Задача 6: 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number_ticket = input("Введите 6-тизначный номер вашего билета: ")

num1 = int(number_ticket[0])
num2 = int(number_ticket[1])
num3 = int(number_ticket[2])
num4 = int(number_ticket[3])
num5 = int(number_ticket[4])
num6 = int(number_ticket[5])

sum1 = num1 + num2 + num3
sum2 = num4 +num5 +num6

if sum1 == sum2:
    print("YES, you ticket is happy")
else:
    print("NO, you ticket is not happy")