# Problem
# Return the largest number in the array without using maxNum().

# Example

# Input:  [5, 3, 9, 1]
# Output: 9

def maxNumNum(array):
    maxNum = float("-inf")

    for n in array:
        if n > maxNum: maxNum = n
    
    return maxNum

array = [5,3,9,1]
print(maxNumNum(array))