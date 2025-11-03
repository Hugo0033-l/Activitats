a1 = input().strip().lower()
a2 = input().strip().lower()

if a1 != a2:
    seta1 = set(a1)
    seta2 = set(a2)
    print(seta1 == seta2)
else:
    print(False)