"""
이중우선순위 q"""

import heapq
def solution(operations):
    answer = []
    heapq.heapify(answer)
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(answer, int(i.split(' ')[-1]))
        elif answer != []:
            if int(i.split(' ')[-1])< 0:
                heapq.heappop(answer)
            else:
                answer = sorted(answer)
                answer.pop(-1)
    if answer == []:
        return [0,0]
    else:
        return [sorted(answer)[-1], sorted(answer)[0]]

"""
k번째 수
"""

def solution(array):
    answer = [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]
    return answer