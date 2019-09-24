s = 'O.O;P'
bad = ['.',';']
for char in bad:
    s = ''.join(s.split(char))
print(s)
