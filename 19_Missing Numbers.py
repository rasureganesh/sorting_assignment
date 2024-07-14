def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [9,6,4,2,3,5,7,0,1]
print("Input:", nums)
print("Output:", missingNumber(nums))  # Output: 2
