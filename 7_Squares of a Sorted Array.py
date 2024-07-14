def sortedSquares(nums):
    n = len(nums)
    squares = [0] * n
    left, right = 0, n - 1
    index = n - 1
    
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            squares[index] = nums[left] ** 2
            left += 1
        else:
            squares[index] = nums[right] ** 2
            right -= 1
        index -= 1
    
    return squares

nums = [-4, -1, 0, 3, 10]
print("Input:", nums)
print("Output:", sortedSquares(nums))  
