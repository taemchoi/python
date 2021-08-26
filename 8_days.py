"""
섬연결
"""

def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    answer  = costs[0][2]
    node = set([costs[0][0], costs[0][1]])
    while len(node)<n:
        for idx, i in enumerate(costs[1:]):
            if i[0] in node and i[1] in node:
                continue
            if i[0] in node or i[1] in node:
                node.update([i[0],i[1]])
                answer += i[2]
                costs[idx+1]= [-1,-1,-1]
    return answer

"""
단속카메라
"""
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) 
    camera = -30001 

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer