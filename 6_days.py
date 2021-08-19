
"""
디스크 컨트롤러
"""
import heapq
def solution(jobs):
    answer,end,count =0,0,0

    start = -1

    new_jobs = []
    while count< len(jobs):
        for i in jobs:
            if start < i[0] <= end:
                heapq.heappush(new_jobs,[i[1],i[0]])


        if len(new_jobs)>0:
            current = heapq.heappop(new_jobs)
            start = end
            end += current[0]
            answer += (end-current[1]) 
            count +=1
        else:
            end +=1
    return int(answer/len(jobs))