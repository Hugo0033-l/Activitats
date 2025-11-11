def read_mobile(lines, index):
    pi, di, pd, dd = lines[index]
    index += 1
    balancejat = True
    if pi == 0:
        pi, sub_balancejat, index = read_mobile(lines, index)
        balancejat = balancejat and sub_balancejat
    if pd == 0:
        pd, sub_balancejat, index = read_mobile(lines, index)
        balancejat = balancejat and sub_balancejat
    if pi*di != pd*dd:
        balancejat = False
    pes_total = pi+pd
    return pes_total, balancejat, index

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
    pes_total, balancejat, index = read_mobile(lines,index)
    if balancejat:
        print("SI")
    else:
        print("NO")