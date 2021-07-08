def square(side):
    p = side * 4
    s = side ** 2
    d = side * (2 ** (1/2))
    print ((p, s, d))

a = int(input())
square(a)
