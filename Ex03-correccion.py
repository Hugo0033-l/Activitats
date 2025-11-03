def is_prime(number:int)->bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3,int(number**0.5)+1, 2):
        if number % i == 0:
            return False
    return True

total = int(input())
for _ in range(total):
    print(is_prime(int(input())))