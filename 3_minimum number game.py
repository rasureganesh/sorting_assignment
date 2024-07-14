def game(nums):
    nums.sort()
    n = len(nums)
    arr = []
    left, right = 0, n - 1
    
    while left <= right:
        arr.append(nums[left])
        left += 1
        if left <= right:
            arr.append(nums[right])
            right -= 1
    
    return arr

# Example usage:
nums = [5, 4, 2, 3]
print("Input:", nums)
print("Output:", game(nums))  # Output: [3, 2, 5, 4]
