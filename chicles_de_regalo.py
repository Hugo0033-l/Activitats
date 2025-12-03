def resolver_chicles():
    while True:
        linea = input().strip()
        n, m, comprados = map(int, linea.split())
        
        # Condición de terminación
        if n == 0 and m == 0 and comprados == 0:
            break
        
        # Caso especial: si no compramos nada
        if comprados == 0:
            print("0 0")
            continue
        
        # Verificar si hay ruina
        # Si por N envoltorios nos dan M chicles y M >= N,
        # entonces nunca se acaban los envoltorios
        if m >= n:
            print("RUINA")
            continue
        
        # Simular el proceso
        total_comidos = comprados
        envoltorios = comprados
        
        # Mientras tengamos suficientes envoltorios para canjear
        while envoltorios >= n:
            # Calculamos cuántos chicles gratis obtenemos
            chicles_gratis = (envoltorios // n) * m
            
            # Calculamos envoltorios sobrantes después del canje
            envoltorios_usados = (envoltorios // n) * n
            envoltorios = envoltorios - envoltorios_usados + chicles_gratis
            
            # Sumamos los chicles gratis al total
            total_comidos += chicles_gratis
        
        print(f"{total_comidos} {envoltorios}")

# Ejecutar el programa
resolver_chicles()