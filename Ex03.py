num = []
casos = int(input())
for i in range(casos):
    num.append(int(input()))

for i in num:
    r = True
    for a in range(2,i):
        if i%a == 0:
            r = False
    print(r)