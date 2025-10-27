for i in range(1,101):
    if i%5 == 0 and i%3 == 0:
        print("FIZZ BUZZ")
    elif i%3 == 0:
        print("FIZZ")
    elif i%5 == 0:
        print("BUZZ")
    else:
        print(i)