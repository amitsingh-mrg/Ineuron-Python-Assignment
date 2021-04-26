suffix = ""
number_divisible_by_7 = ""
start = 2000
while start % 7 != 0:
    start += 1
for x in range(start, 3201, 7):
    number_divisible_by_7 += suffix + str(x)
    suffix = ","
print(number_divisible_by_7)
