casos = int(input().strip())

for i in range(casos):
    a = input().strip()
    e = a.split()
    for o in range(len(e)):
        e[o] = int(e[o])
    distancia = ((e[0]**2)+(e[1]**2))**0.5
    print(int(distancia))