"""
완주 선수 
"""
def solution(participant, completion):
    answer_dict = {}
    hash_values = 0
    for p in participant:
        answer_dict[hash(p)] = p
        hash_values += hash(p)
    for c in completion:
        hash_values -= hash(c)
    return answer_dict[hash_values]
    

"""
전화번호목록
"""
# 1차 시도
from collections import Counter

def hash_func(key, length):
    if len(key)-length !=0:
        return float(key)/(10^(len(key)-length))
    else:
        return float(key) * (10^(len(key)-length)) *100
    

def solution(phone_book):
    if 1 <= len(phone_book) <= 1000000 and sorted(Counter(phone_book).values())[-1] == 1:
        for i in phone_book:
            if 1 <= len(i) <= 20:
                legnth =len(i)
                for j in phone_book:
                    if hash_func(j, legnth) - float(i)  < 1:
                        print(hash_func(j, legnth))
                        return False 
    answer = True
    return answer


# 2차 시도 
from collections import Counter
def solution(phone_book):
    if 1 <= len(phone_book) <= 1000000 and sorted(Counter(phone_book).values())[-1] == 1:
        phone_book.sort()
        for p1, p2 in zip(phone_book, phone_book[1:]):
            if 1 <= len(p1) <= 20 and 1 <= len(p2 <= 20 and  p2.startswith(p1)):
                return False
        return True