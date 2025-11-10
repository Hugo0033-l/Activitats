def read_mobile(linea, index):
    pi, di, pd, dd = lines[index]
    index += 1
    blancetjat = True
    if pi == 0:
        read_mobile(lines, index)

lines = []
while True:
    line = input().strip()
    if not line:
        continue
    nums = list(map(int, line.split()))

    if nums == [0,0,0,0]:
        break

    lines.append(nums)

index = 0
while index < len(lines):
    ...
    #______ = read_mobile(lines,index)