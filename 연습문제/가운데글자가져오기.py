import math

# def solution(s):
#     answer = ''
#     if len(s) % 2 ==0:
#         answer = s[math.floor(len(s)/2)-1:math.floor(len(s)/2)+1]
#     else:
#         answer = s[math.floor(len(s)/2)]
#     return answer

def solution(s):
    answer = ''
    answer = s[(len(s)-1)//2:len(s)//2+1]
    return answer

print(solution('power'))
print(solution('milk'))