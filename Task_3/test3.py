import math

filename = 'text_3_var_28'
with open(filename) as file:
    lines = file.readlines()

matrix = list()

for line in lines:
    # print (line.strip())
    nums = line.strip().split(",")
    for i in range(len(nums)):
        if nums[i] == 'NA':
            nums[i] = str((int(nums[i - 1]) + int(nums[i + 1])) / 2)

    filtered = list()
    for item in nums:
        num = float(item)
        if math.sqrt(num) > 78:
            filtered.append(num)

    matrix.append(filtered)

with open('text_3_result.txt', 'w') as result:
    for row in matrix:
        for num in row:
            result.write(str(num) + ',')
        result.write("\n")