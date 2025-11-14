paises = [
        ["0", "380", "50", "539", "560", "70", "759", "850", "890"],
        ["EEUU", "Bulgaria", "Inglaterra", "Irlanda", "Portugal", "Noruega", "Venezuela", "Cuba", "India"]
]

def comprovar_codigo(codigo:str)->str:
    lista = []
    factor = 0
    sec = ""

    if len(str(codigo))==8:
        multiplicar = 3
    else:
        multiplicar = 1
        sec = "Desconocido"

    for i in range(3):
        if codigo[:i] in paises[0]:
            sec = paises[1][paises[0].index(codigo[:i])]

    for i in range(0,len(str(codigo))-1):
        lista.append(int(codigo[i])*multiplicar)
        if multiplicar == 3:
            multiplicar = 1
        else:
            multiplicar = 3

    for i in lista:
        factor += i

    if (factor+int(codigo[-1]))%10 == 0:
        return f"SI {sec}"
    else:
        return "NO"

num = []
while True:
    r = input()
    if not r:
        continue
    if r != "0":
        num.append(r)
    else:
        break
for i in num:
    print(comprovar_codigo(i))