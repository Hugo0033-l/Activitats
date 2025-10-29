while True:
    res = input().strip()
    if res == "0 0 0 0":
        break
    if res[2] == "0":
        print("add left")
    if res[-1] == "0":
        print("add right")