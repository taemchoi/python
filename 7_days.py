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


"""
가장큰수
"""

def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse=True)
    return str(int(''.join(numbers_str)))


"""
완전탐색
"""

def solution(answers):
    answer = []
    a = [1,2,3,4,5]*8
    b = [2,1,2,3,2,4,2,5]*5
    c = [3,3,1,1,2,2,4,4,5,5]*4
    if len(a) < len(answers):
        num = (len(answers)//len(a)+1)
        a *=num
        b *=num
        c *=num
    count = [0,0,0]
    for idx, i in enumerate(answers):
        if a[idx] == i:
            count[0]+=1
        if b[idx] == i:
            count[1]+=1
        if c[idx] == i:
            count[2]+=1
    for idx, i in enumerate(count, start=1):
        if i>=max(count):
            answer.append(idx)
    return answer


"""
카펫
"""

def solution(brown, yellow):
    num = brown+yellow
    a = []
    for i in range(1, num+1):
        if num%i==0 and (i-2)*(num//i-2) == yellow:
            return [num//i, i]

"""
체육복
"""

def solution(n, lost, reserve): 
    reser_del = set(reserve)-set(lost) 
    lost_del = set(lost)-set(reserve) 
    for i in reser_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
    return n-len(lost_del)