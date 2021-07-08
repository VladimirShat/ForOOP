#Checking whether the strings contain the same number of identical chars

str1 = 'aaba'
s1 = set(str1)
d1 = dict()
for element in s1:
    d1[element] = list(str1).count(element)

str2 = 'baaa'
s2 = set(str2)
d2 = dict()
for element in s2:
    d2[element] = list(str2).count(element)

if d1 == d2:
    print(d1)
    print(d2)
