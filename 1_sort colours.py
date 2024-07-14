def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums

nums = [2, 0, 2, 1, 1, 0]
print("Input:", nums)
print("Output:", sortColors(nums))  
