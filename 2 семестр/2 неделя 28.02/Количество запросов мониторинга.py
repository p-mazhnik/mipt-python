f = open('input.txt')
a = 0
for line in f:
    if "Go-http-client/1.1" in line:
        a += 1
f.close()
print a
