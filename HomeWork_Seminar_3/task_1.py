# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1

n = int(input('Введите количество элементов списка А: '))
numbers_array = input("Введите через пробел элементы списка: ").split()
array_A = list(map(int, numbers_array))
if len(array_A) != n:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(n):
        if array_A[i] == x:
            count += 1
    print(f'Число {x} встречается в списке A {count} раз') 
    


