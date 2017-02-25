a = []
for i in range(1, 101):
    print (i, end=' ')
    a.append(i)
flag = 1
print ()
for i in a:
    if flag % 15 == 0:
        a[i - 1] = 'BazQux'
    elif flag % 5 == 0:
        a[i - 1] = 'Qux'
    elif flag % 3 == 0:
        a[i - 1] = 'Baz'
    flag += 1
    print (a[i - 1], end=' ')
