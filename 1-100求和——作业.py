def sum_of_numbers(x, y):
    total = 0
    for i in range(x, y + 1):
        total += i
    return total


# 使用函数计算1到100的和
sum_of_1_to_100 = sum_of_numbers(1, 100)

print(sum_of_1_to_100)