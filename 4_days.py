"""
다리지나는 트럭
"""
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while len(bridge) != 0:
        time +=1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0]<weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time


"""
주식가격
"""
def solution(prices):
    answer =[0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer
