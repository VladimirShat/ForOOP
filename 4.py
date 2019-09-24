data = '14 * x^2 + 20 * x + 2'
f,s,t = 0,1,2
if data[0] == '-':
    f,s,t = 1,2,3
data = data.replace('-', '+-')
k = data.split('+')
k = [k[f].split('*'),
       k[s].split('*'),
       k[t].split('*')]
print(k)

a,b,c = float(k[0][0]), float(k[1][0]), float(k[2][0])
d = b*b - 4 * a * c

if d > 0:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print('x1 = ' + str(x1) + ' x2 = ' + str(x2))
elif d == 0:
    x = (-b / 2 * a)
    print('x = ' + str(x))
else:
    print('no roots')
