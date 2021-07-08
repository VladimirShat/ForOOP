def bank(a, years):
    for i in range(years):
        a = a * 1.1
    print (a)

a = int(input("Введите сумму вклада: "))
years = int(input("Введите кол-во лет: "))
bank(a, years)
