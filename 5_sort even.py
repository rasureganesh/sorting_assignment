def rearrangeArray(nums):
    n = len(nums)
    
    # Step 1: Separate odd and even indexed elements
    odd_indices = [nums[i] for i in range(1, n, 2)]
    even_indices = [nums[i] for i in range(0, n, 2)]
    
    # Step 2: Sort according to the rules
    odd_indices.sort(reverse=True)
    even_indices.sort()
    
    # Step 3: Reconstruct nums with sorted values
    for i in range(1, n, 2):
        nums[i] = odd_indices.pop(0)
    for i in range(0, n, 2):
        nums[i] = even_indices.pop(0)
    
    return nums

# Example usage:
nums = [4, 1, 2, 3]
print("Input:", nums)
print("Output:", rearrangeArray(nums))  # Output: [2, 3, 4, 1]
