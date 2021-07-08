def is_prime(number):
    k = 0
    for i in range(2, number):
        # ищем количество делителей
        if number % i == 0:
            k = k + 1
    # если делителей нет, добавляем число в список
    if k == 0:
        print(True)
    else:
        print(False)

number = int(input())
is_prime(number)
