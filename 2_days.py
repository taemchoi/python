"""
위장
"""
def solution(clothes):  
    a= {}
    for i in clothes:
        if i[-1] in a:
            a[i[-1]] +=1
        else:
            a[i[-1]]=1
    count= 1

    for i,j in a.items():
        count*=(j+1)
    answer= count-1
    return answer


    