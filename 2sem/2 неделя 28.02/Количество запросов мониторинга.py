a = 0
f = open('input.txt')
for line in f:
    if '"Go-http-client/1.1"' in line:
        a += 1
f.close()
print a
