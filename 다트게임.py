# def solution(dartResult):
#     import re
#     from collections import deque
#     score = []
#     su = deque(re.findall("(\d+)",dartResult))
#     while True:
#         if not dartResult: return sum(score)
#         s = su.popleft()
#         dartResult = dartResult[len(s):]
#         s = int(s)
#         b = dartResult[0]
#         dartResult = dartResult[1:]
#         if b == 'S': score.append(s)
#         elif b == 'D': score.append(s**2)
#         elif b == 'T': score.append(s**3)
#         if not dartResult: return sum(score)
#         if dartResult[0]=='*' or dartResult[0]=='#':
#             o = dartResult[0]
#             dartResult = dartResult[1:]
#             if o == '*':
#                 if len(score)<2:
#                     score[-1]*=2
#                 else:
#                     score[-1]*=2
#                     score[-2]*=2                    
#             else:
#                 score[-1]*=(-1)
#     return sum(score) 

def solution(dartResult):
    import re
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'':1, '*':2, '#':-1}
    dart = re.findall('(\d+)([SDT])([*#]?)',dartResult)
    for i in range(len(dart)):
        if dart[i][2]=='*' and i>0:
            dart[i-1]*=2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    return sum(dart)

# print(solution("1S2D*3T"))
# print(solution("1D2S#10S"))
print(solution("1D2S0T"))
# print(solution("1S*2T*30S"))