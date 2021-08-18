"""
더맵게
"""
# 1차 시도 : 시간초과
def solution(scoville, K):
    answer = 0
    for i in range(len(scoville)):
        scoville[0] = scoville.pop(0) + (scoville[0]*2)
        answer +=1
        if any(j<K for j in scoville) == False:
            break

    return answer

# 2차 시도 : confirm
import heapq
def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    while scoville[0]< K:
        new = heapq.heappop(scoville) +(heapq.heappop(scoville) *2)
        heapq.heappush(scoville, new)
        answer += 1
        if len(scoville) ==1 or scoville[0] < K:
            return -1
    return answer