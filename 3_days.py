"""
베스트 앨범
"""

from collections import defaultdict
def solution(genres, plays):
    dic = defaultdict(int)
    lis = defaultdict(list)
    for idx,(i, j) in enumerate(zip(genres,plays)):
        lis[i].append((j, idx))   
        dic[i] += j
    dic=sorted(dic.items(), key=lambda x: x[1],reverse=True)
    answer=[]
    count = 0   
    for d in dic:
        answer.extend([id for num, id in sorted(lis[d[0]], key=lambda x: (-x[0], x[1]))[:2]])
    return answer



"""
기능개발
"""
import math
def solution(progresses, speeds):
    rest=[math.ceil((100 - i)/j) for i, j in zip(progresses, speeds)]
    count = 1
    idx = 0
    answer = []
    for i in range(1,len(rest)):
        if rest[idx]>=rest[i]: 
            count +=1

        else:
            idx=i
            answer.append(count)
            count = 1
    answer.append(count)
    return answer


"""
프린터
"""
def solution(priorities, location):
    idx = 1
    jdx = 0
    b=[i for i in range(len(priorities))]

    while jdx < len(priorities):
        if priorities[jdx] < priorities[idx]: 
            priorities.append(priorities[jdx])
            b.append(b[jdx])
            priorities.pop(jdx)
            b.pop(jdx)
            idx=jdx
        idx+=1
        if idx ==len(priorities):
            jdx += 1
            idx = jdx
    return b.index(location)+1