def heightChecker(heights):
    expected = sorted(heights)
    
    mismatches = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            mismatches += 1
    
    return mismatches

heights = [1, 1, 4, 2, 1, 3]
print("Input:", heights)
print("Output:", heightChecker(heights))  
