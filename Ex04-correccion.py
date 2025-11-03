def decimal_to_binari(decimal:int) -> str:
    if decimal < 2:
        return str(decimal)
    return decimal_to_binari(decimal//2) + str(decimal%2)

total = int(input())
for _ in range(total):
    print(decimal_to_binari(int(input())))