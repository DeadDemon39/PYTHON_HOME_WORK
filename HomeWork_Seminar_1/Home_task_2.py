# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# Общее кол-во готовых журавликов = S
s = int(input("Сколько всего журавликов было сделано?: "))

num1 = s // 3
num2 = num1 // 2
num_Kate = num1 + num1

print(f"Петя и Сережа сделали по {num2} журавликов, а Катя сделала {num_Kate} журавликов.")



# ВТОРОЙ ВАРИАНТ РЕШЕНИЯ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

s = int(input("Введите количество сделанных журавликов: "))

n1 = s // 6
n2 = n1
n3 = (n1 + n2) * 2

print(f"Петя сделал {n1} журавликов, Сережа сделал {n2} журавликов, а Катя сделала {n3} журавликов.")
