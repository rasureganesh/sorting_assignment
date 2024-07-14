def findRanks(score):
    n = len(score)
    sorted_score = sorted(score, reverse=True)
    
    answer = [""] * n
    
    for i in range(n):
        if i == 0:
            answer[score.index(sorted_score[i])] = "Gold Medal"
        elif i == 1:
            answer[score.index(sorted_score[i])] = "Silver Medal"
        elif i == 2:
            answer[score.index(sorted_score[i])] = "Bronze Medal"
        else:
            answer[score.index(sorted_score[i])] = str(i + 1)
    
    return answer

score = [5, 4, 3, 2, 1]
print("Input:", score)
print("Output:", findRanks(score))  
