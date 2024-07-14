def leftoverMoney(prices, money):
    prices.sort()
    
    left = 0
    right = len(prices) - 1
    min_leftover = money
    
    while left < right:
        current_sum = prices[left] + prices[right]
        
        if current_sum <= money:
            min_leftover = min(min_leftover, money - current_sum)
            left += 1  
        else:
            right -= 1  
    
    if min_leftover == money:
        return money
    return min_leftover

prices = [3,2,3]
money = 3
print("Input: prices =", prices, "money =", money)
print("Output:", leftoverMoney(prices, money))  # Output: 0
