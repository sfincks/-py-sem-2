
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число n: "))
sum = []
temp = 0
i = 0
while temp <= n:
    temp = 2**i
    if temp > n:
        break
    else:
        i += 1
        sum.append(temp)
print(*sum)
