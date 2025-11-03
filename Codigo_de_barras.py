codigo = input()
lista = []
factor = 0
sec = ""
paises = [
    ["0", "380", "50", "539", "560", "70", "759", "850", "890"],
    [1, 3, 2, 3, 3, 2, 3, 3, 3]
    ["EEUU", "Bulgaria", "Inglaterra", "Irlanda", "Portugal", "Noruega", "Venezuela", "Cuba", "India"]
]

if len(str(codigo))==8:
    multiplicar = 3
else:
    multiplicar = 1
    sec = "Desconocido"

for i in range(0,len(str(codigo))-1):
    lista.append(int(codigo[i])*multiplicar)
    if multiplicar == 3:
        multiplicar = 1
    else:
        multiplicar = 3

for i in lista:
    factor += i

if (factor+int(codigo[-1]))%10 == 0:
    print("SI")
else:
    print("NO")