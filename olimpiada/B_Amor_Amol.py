casos = int(input().strip())

for i in range(casos):
    frase = input().strip().lower()
    frase = frase.replace("l", "r")
    print(frase)