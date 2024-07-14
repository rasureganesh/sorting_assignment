def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
    
    return result

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print("Input:", nums)
print("Output:", findDisappearedNumbers(nums))  # Output: [5, 6]
