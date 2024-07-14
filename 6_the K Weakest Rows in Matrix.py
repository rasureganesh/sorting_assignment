import heapq

def kWeakestRows(mat, k):
    # Step 1: Compute soldier counts for each row
    heap = []
    
    for i in range(len(mat)):
        soldier_count = sum(mat[i])
        heapq.heappush(heap, (soldier_count, i))
        
    # Step 2: Extract the k weakest rows from the heap
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    
    return result

# Example usage:
mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3
print("Input:")
for row in mat:
    print(row)
print("k =", k)
print("Output:", kWeakestRows(mat, k))  
