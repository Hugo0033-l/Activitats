
while True:
    categoria = input().strip()
    if categoria == "FIN":
        break

    punts = {}
    partits_jugats = 0
    while True:
        linia = input().strip()
        if linia == "FIN":
            break
        format_line = linia.split()
        parella_casa = format_line[0]
        sets_casa = int(format_line[1])
        parella_visit = format_line[2]
        sets_visit = int(format_line[3])

        if parella_casa not in punts:
            punts[parella_casa] = 0
        if parella_visit not in punts:
            punts[parella_casa] = 0

        if sets_casa > sets_visit:
            punts[parella_casa] += 2
            punts[parella_visit] += 1
        else:
            punts[parella_casa] += 1
            punts[parella_visit] += 2

        partits_jugats += 1
    
    max_punts = max(punts.values())

    guanyadors = [parella for parella, punts in punts.items() if punts == max_punts]

    #guanyadors = list(filter(lambda parella: punts[parella] == max_punts, punts.keys()))

    """
    guanyadors = []
    for parella, punts in punts.items():
        if punts == max_punts:
            guanyadors.append(parella)
    
    parella_guañadora = ""
    if len(guanyadors) > 1:
        parella_guañadora = "EMPAT"
    else:
        parella_guañadora = guanyadors[0]
    """

    """
    parella_guanyadora = ""
    for parella, punts in punts.items():
        if parella_guanyadora != "" and punts == max_punts:
            parella_guanyadora = parella
        elif punts == max_punts:
            parella_guanyadora = "EMPAT"
    """  
