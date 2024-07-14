from collections import Counter

def frequencySort(nums):
    freq = Counter(nums)
    
    sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
    
    return sorted_nums

nums = [1, 1, 2, 2, 2, 3]
print("Input:", nums)
print("Output:", frequencySort(nums))  
