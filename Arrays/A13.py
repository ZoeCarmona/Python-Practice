# Problem: Best Time to Buy and Sell Stock
# Return the maximum profit you can achieve.

# Input:  [7,1,5,3,6,4]
# Output: 5
def max_profit(prices):
    

    for n in prices:
        if n < minNum:
            minNum = n

    return minNum

prices = [7,1,5,3,6,4]

print(max_profit(prices))