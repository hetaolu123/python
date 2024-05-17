def maximumProduct(nums):
    # 对数组进行排序
    nums.sort()
    n = len(nums)

    # 计算第一种情况：三个最大的数相乘
    product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]

    # 如果数组长度小于3或者没有负数，那么第一种情况就是答案
    if n < 3 or nums[0] >= 0:
        return product1

        # 计算第二种情况：两个最小的负数和一个最大的正数相乘
    product2 = nums[0] * nums[1] * nums[n - 1]

    # 返回两种情况中的较大值
    return max(product1, product2)


# 示例用法
nums = [1, 2, 3, 4]
print(maximumProduct(nums))  # 输出: 24

nums = [-2, 0, -1]
print(maximumProduct(nums))  # 输出: 0，因为存在0，所以最大乘积为0

nums = [-2, -3, -1, 5, 6, 4]
print(maximumProduct(nums))  # 输出: 180，因为5 * 6 * (-3) > 6 * 5 * 4