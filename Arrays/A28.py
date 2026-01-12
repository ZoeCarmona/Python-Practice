# Problem: Partition Array Into Three Parts With Equal Sum
# Return True if the array can be split into three contiguous parts with equal sum.

# Input:  [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: True

def can_three_parts_equal_sum(arr):
    total = sum(arr)

    if total % 3 != 0:
        return False

    target = total // 3
    parts = 0
    current = 0

    for x in arr:
        current += x
        if current == target:
            parts += 1
            current = 0
            if parts == 2:   
                return True

    return False

print(can_three_parts_equal_sum([0,2,1,-6,6,-7,9,1,2,0,1]))