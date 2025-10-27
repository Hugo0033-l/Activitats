nums = []
value = False

while True:
    entrada = int(input())
    if entrada != 0:
        nums.append(entrada)
    else:
        break

for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        print("error")
        value = True

if value == False and len(nums) > 1:
    for i in range(nums[1],nums[-1]):
        if i not in nums:
            print(i)