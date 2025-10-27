ngiven_r = True
ngiven_v = True
ngiven_i = True

v = 0 
i = 0
r = 0

do = True
responses = 0

while True:
    response = input().strip()
    responses += 1
    if response == "0":
        responses -= 1
        break
    if response[2] == "0":
        do = False
    if response[0] == 'V':
        v = float(response[2:])
        ngiven_v = False
    if response[0] == 'I':
        i = float(response[2:])
        ngiven_i = False
    if response[0] == 'R':
        r = float(response[2:])
        ngiven_r = False

if responses != 2:
    do = False

if do:
    if ngiven_r:
        res = v/i
        unit = "R"
    if ngiven_i:
        res = v/r
        unit = "I"
    if ngiven_v:
        res = i*r
        unit = "V"

    res = str(res)
    point = res.find(".")
    res = res[:point+3]

    print(unit+" "+res)
else:
    print("Invalid values")


