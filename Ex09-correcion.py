# Llegir les dades
elements = {}
while True:
    string = input()
    if string == "0":
        break
    letter = string[0]
    value = int(string[2:])
    elements[letter] = value

try:
    if len(elements) != 2 or not set(elements.keys()).issubset({"I","V","R"}):
        print("Invalid values")
    else:
        if "V" not in elements:
            result = elements["I"]*elements["R"]
            print(f"V {result}")
        if "R" not in elements:
            result = elements["V"]/elements["I"]
            print(f"R {result}")
        if "I" not in elements:
            result = elements["V"]/elements["R"]
            print(f"I {result}")
except(ValueError, ZeroDivisionError, KeyError):
    print("Invalid values")