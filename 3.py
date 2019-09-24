s1 = 'aaba'
se1 = set(s1)
d1 = dict()
for element in se1:
    d1[element] = list(s1).count(element)

s2 = 'baaa'
se2 = set(s2)
d2 = dict()
for element in se2:
    d2[element] = list(s2).count(element)
    
if d1 == d2:
    print(d1)
    print(d2)
    print('da')
