num = int(input())

def fibonacci(number:int):
    if number == 1 or number == 2:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
print(fibonacci(num))