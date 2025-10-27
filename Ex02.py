a1 = input().strip().lower()
a2 = input().strip().lower()

if a1 != a2:
    seta1 = set(a1)
    seta2 = set(a2)
    if seta1 == seta2:
        print(True)
    else:
        print(False)
else:
    print(False)