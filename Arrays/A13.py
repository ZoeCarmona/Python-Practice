# Problem: Best Time to Buy and Sell Stock
# Return the maximum profit you can achieve.

# Input:  [7,1,5,3,6,4]
# Output: 5
def max_profit(prices):
    minNum = float('inf')
    best = 0
    for price in prices:
        if price < minNum:
            minNum = price
        else:
            best = max(best, price - minNum)

    return best

prices = [7,1,5,3,6,4]

print(max_profit(prices))