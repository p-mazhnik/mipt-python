s = {"Ubuntu:": 0, "Unknown:": 0, "OS X:": 0, "Windows:": 0}
f = open('input.txt')
for line in f:
    k = line.split('" "')
    line1 = k[1]
    if line1.find("Ubuntu") != -1:
        s["Ubuntu:"] += 1
    elif line1.find("Macintosh") != -1:
        s["OS X:"] += 1
    elif line1.find("Windows") != -1:
        s["Windows:"] += 1
    else:
        s["Unknown:"] += 1
f.close()
for k, v in sorted(s.items(), key=lambda x: x[1]):
    print k, v
