EFECTIVITAT = {
    "Aigua": {"efectiu": {"Foc"},
              "no_efectiu": {"Aigua", "Planta"}},
    "Foc": {"efectiu": {"Planta"},
              "no_efectiu": {"Foc", "Aigua"}},
    "Planta": {"efectiu": {"Aigua"},
              "no_efectiu": {"Planta", "Foc"}},
    "Elèctric": {"efectiu": {"Aigua"},
              "no_efectiu": {"Elèctric", "Planta"}}
}

def potencia(tipo_atacant, tipo_defensor, valor_atac, valor_defensa):
    if valor_atac < 0 or valor_defensa < 0:
        return "error"
    efectivitat = 1
    if tipo_defensor in EFECTIVITAT[tipo_atacant]["efectiu"]:
        efectivitat = 2
    elif tipo_defensor in EFECTIVITAT[tipo_atacant]["no_efectiu"]:
        efectivitat = 0.5

    return 50 * (valor_atac/valor_defensa) * efectivitat

atacant = input()
defensor = input()
v_atac = int(input())
v_def = int(input())
print(potencia(atacant,defensor,v_atac,v_def))