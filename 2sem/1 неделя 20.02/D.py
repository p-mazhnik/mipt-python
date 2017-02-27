flag = 0
a = 0.0
b = 1
for i in range(1, 11):
    if flag % 2 == 0:
        a += 4/b
    else:
        a -= 4/b
    flag += 1
    b += 2
print (a)
