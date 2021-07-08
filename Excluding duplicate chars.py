s = 'Hello,,, world!!!'
l = list(s)
i = 0
for char in l:
    if char != l[0] and not char.isalnum() and l[i - 1] == char and char != ' ':
        l[l.index(char)] = ''
    i += 1
print(''.join(l))
