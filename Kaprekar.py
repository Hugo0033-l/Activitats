def iter_kaprekar(num:int):
    if num == 6174:
        return 0
    
    num_str = str(num).zfill(4)

    if len(set(num_str)) == 1:
        return 8
    
    iteracions = 0
    actual = num

    while actual != 6174:
        num_str = str(actual).zfill(4)
        ascendent = int("".join(sorted(num_str)))
        descendent = int("".join(sorted(num_str, reverse=True)))

        actual = descendent - ascendent
        iteracions+=1

        if iteracions > 7:
            break

    return iteracions

def keprekar(case:str)->int:
    res = 0
    tries = 0
    while case != "6174":
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
        if tries > 7:
            break
        if res != 6174:
            tries += 1
            case = str(res)
            if len(case) < 4:
                case += "0"*(4-len(case))
        else:
            tries += 1
            break
    return tries

num = []
casos = int(input())
for i in range(casos):
    num.append(input())
for i in num:
    print(iter_kaprekar(i))