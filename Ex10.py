tipus_atacant = input().lower().strip()
tipus_defensor = input().lower().strip()
atac = int(input())
defensa = int(input())

efectivitat = 1

tipus = ["aigua", "foc", "planta", "elèctric"]

taula_efectivitat = [[0.5, 2, 0.5, 1],
[0.5, 0.5, 2, 1],
[2, 0.5 , 0.5, 1],
[2, 1, 0.5, 0.5]]

while True:
    if atac < 0 or atac > 100 or defensa < 0 or defensa > 100 or tipus_atacant not in tipus or tipus_defensor not in tipus:
        print("Error")
        break
    pos1 = int(tipus.index(tipus_atacant))
    pos2 = int(tipus.index(tipus_defensor))
    efectivitat = taula_efectivitat[pos1][pos2]

    ad = atac/defensa

    print(50*ad*efectivitat)
    break