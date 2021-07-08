#Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
#Начиная с 1 и 2, первые 10 элементов будут:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают 4 млн.

import time
start=time.time()
#Код
prev = 1
current = 1
sum = 0
while(current <= 4000000):
    if current % 2 == 0:
        sum += current
    temp = current
    current += prev
    prev = temp
print(sum)
#Код
print(str(time.time()-start) + " сек.")
