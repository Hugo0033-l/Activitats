casos = int(input().strip())

for i in range(casos):
    a = int(input().strip())
    if a % 2 != 0:
        a += 1
    a = a//2
    print(a)
