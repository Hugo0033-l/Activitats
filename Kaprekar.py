def keprekar(case:str, tries = 0)->int:
    list_num = list(case)
    list_num.sort()
    a = list_num.copy()
    list_num.sort(reverse=True)
    b = list_num.copy()
    a = int("".join(a))
    b = int("".join(b))
    if a > b:
        res = a-b
    else:
        res = b-a
    
    print(res)
    if res != 6174:
        print(tries)
        keprekar(str(res), tries=tries+1)
    else:
        print(tries)
        return tries
    

num = []
casos = int(input())
for i in range(casos):
    num.append(input())

for i in num:
    a = keprekar(i)
    print(a)