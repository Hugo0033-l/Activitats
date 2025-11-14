def calcular_digit_contrl(digits):
    suma = 0
    for n, d in enumerate(reversed(digits[:-2]), 1):
        digit = int(d)

        if n % 2 == 1:
            suma += digit * 3
        else:
            suma += digit

    digit_control = (10-(suma%10)) % 10
    return digit_control

