# def solution(participant, completion):
#     _par = [i for i in participant]
#     _com = [i for i in completion]
#     result = []
#     for value in _par:
#         if value not in _com:
#             result.append(value)
#         else:
#             _com.pop(_com.index(value))
#     return ''.join(result)

# def solution(participant, completion):
#     _par = {x:participant.count(x) for x in participant}
#     _com = {x:completion.count(x) for x in completion}
#     for key in _com.keys():
#         _par[key]-=_com[key]
#     for key in _par.keys():
#         if _par[key]!=0: 
#             result = key
#             break
#     return result

# import collections
# def solution(participant, completion):
#     _par = collections.Counter(participant)
#     _com = collections.Counter(completion)
#     for key in _par.keys():
#         if key in _com:
#             _par[key]-=_com[key]
#         if _par[key]!=0: 
#             result = key
#             break
#     return result

import collections
def solution(participant, completion):
    result = collections.Counter(participant) - collections.Counter(completion)
    print(list(result.keys())[0])

# def solution(participant, completion):
#     temp = 0
#     dic = {}
#     for p in participant:
#         dic[hash(p)] = p
#         temp += hash(p)
#     for c in completion:
#         temp -= hash(c)
#     return dic[temp]

print(solution(["leo","kiki","eden"],["leo","kiki"]))