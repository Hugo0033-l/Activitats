num = []
casos = int(input().strip())
for i in range(casos):
    num.append(int(input().strip()))

for i in num:
    binari = ""
    a = i
    if a == 0:
        binari = "0"
    while a != 0:
        if a%2 == 0:
            binari += "0"
        else:
            binari += "1"
        a = a//2
    binari = binari[::-1]
    print(binari)