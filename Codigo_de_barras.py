codigo = input()
lista = []
factor = 0


multiplicar = 3
for i in range(0,7):
    lista.append(int(codigo[i])*multiplicar)
    if multiplicar == 3:
        multiplicar = 1
    else:
        multiplicar = 3

for i in lista:
    factor += i

if (factor+int(codigo[-1]))%10 == 0:
    print("si")
else:
    print("no")