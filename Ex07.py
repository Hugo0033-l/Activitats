my_string = input().strip().lower()
na = ["a","á","à","ä"]
ne = ["e","é","è","ë"]
ni = ["i","í","ì","ï"]
no = ["o","ó","ò","ö"]
nu = ["u","ú","ù","ü"]
a = 0
e = 0
i = 0
o = 0
u = 0

for num in my_string:
    if num in na:
        a += 1
    if num in ne:
        e += 1
    if num in ni:
        i += 1
    if num in no:
        o += 1
    if num in nu:
        u += 1

if a > 0:
    print(f"a {a}")
if e > 0:
    print(f"e {e}")
if i > 0:
    print(f"i {i}")
if o > 0:
    print(f"o {o}")
if u > 0:
    print(f"u {u}")