a = 0
while a <= 10:
    a += 1
    if a%7 == 0:
        continue
    print(a)

while a > 10:
    a +=1
    B = str(a)
    C = B[0:1]
    d = int(C)
    E = B[1:2]
    f = int(E)
    if a%7 == 0 or d == 7 or f == 7:
        continue
    if a > 100:
        break
    print(a)
