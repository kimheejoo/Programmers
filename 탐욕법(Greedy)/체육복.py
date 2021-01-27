# 5,7 Non Pass
# def solution(n, lost, reserve):
#     have = [1]*n # 체육복 가진 사람=1 아니면 0
#     give = [0]*n # 빌려준 사람=1 아니면 0 -> 두 번 빌려줌을 방지하기 위해
#     reserve = [i-1 for i in reserve] # index 헷갈려서 -1 함 [0,2,4]
#     for i in lost:
#         have[i-1] = 0 # lost면 체육복 안가졌으니 flag=0 [1,0,1,0,1]
#     for i in reserve: #여분 가진 사람 [0,2,4]
#         if give[i]==0:
#             if have[i]==0: have[i]=1
#             elif i==n-1:
#                 if have[i-1]==0: have[i-1]=1
#             elif i==0:
#                 if have[i+1]==0: have[i+1]=1
#             else:
#                 if have[i-1]==0:have[i-1]=1
#                 elif have[i+1]==0: have[i+1]=1
#             give[i]=1
#     return have.count(1) 

def solution(n, lost, reserve):
    _lost = [i for i in lost if i not in reserve]
    _reserve = [i for i in reserve if i not in lost]
    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)
    return n-len(_lost)

print(solution(5,[3,4,5],[2,3,4]))