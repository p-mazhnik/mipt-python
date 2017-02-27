a = 0
b = 0
c = 0
f = open('input.txt')
for line in f:
    s = line.split(' ')
    if s[8] == '200':
        a += 1
    elif 300 <= (int)(s[8]) < 310:
        b += 1
    else:
        c += 1
f.close()
print a
print b
print c
print a + b + c
