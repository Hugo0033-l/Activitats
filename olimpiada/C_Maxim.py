casos = int(input().strip())

for i in range(casos):
    nada = input()
    numeros = input().strip()
    num = numeros.split()
    for e in range(len(num)):
        num[e] = int(num[e])
    num.sort()
    max = num[-1]
    count = num.count(max)
    print(f"{max} {count}")