def specialArray(nums):
    nums.sort()
    n = len(nums)
    
    for x in range(1, n + 1):
        count = sum(1 for num in nums if num >= x)
        if count == x:
            return x
    
    return -1

nums = [3, 5]
print("Input:", nums)
print("Output:", specialArray(nums)) 
