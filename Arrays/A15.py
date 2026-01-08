# Problem: Product of Array Except Self
# Return an array where each element is the product of all elements except itself.

# Rules:

# No division

# O(n) time

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# def product_except_self(nums):
#     productRes = 1
#     product = []
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 productRes *= nums[j]
#         product.append(productRes)
#         productRes = 1
#     return product
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

nums = [1,2,3,4]
print(product_except_self(nums))