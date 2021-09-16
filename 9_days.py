
# 정수 삼각현
import copy
def solution(triangle):
    memo = 0
    for idx, i in enumerate(triangle[:-1]):
        comp = triangle[idx+1].copy()
        memo = triangle[idx+1]
        for j in range(len(i)):
            first = i[j] + comp[j] 
            second = i[j] + comp[j+1]
            if  first >= memo[j]: 
                memo[j] = first
            if  second >= memo[j+1]:          
                memo[j+1] = second
        triangle[idx+1] = memo
        
    answer=max(triangle[-1])
    return answer