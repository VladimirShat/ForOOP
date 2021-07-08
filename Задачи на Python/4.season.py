def season(month):
    if month == 12 or month == 1 or month == 2:
        print('зима')
    if month == 3 or month == 4 or month == 5:
        print('весна')
    if month == 6 or month == 7 or month == 8:
        print('лето')
    if month == 9 or month == 10 or month == 11:
        print('осень')

season(int(input()))
