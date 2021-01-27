# def solution(priorities, location):
#     from collections import deque
#     together = deque([f'{chr(65+i)}:{priorities[i]}' for i in range(len(priorities))])
#     location = together[location]
#     finish = []
#     while len(finish)<=len(priorities):
#         if len(together):
#             a = together.popleft()
#         else: 
#             finish.append(a)
#             break
#         for idx,j in enumerate(together):
#             if a.split(':')[1] < j.split(':')[1]:
#                 together.append(a)
#                 break
#             if idx==len(together)-1:
#                 finish.append(a)
#     return finish.index(location)+1

def solution(priorities, location):
    from collections import deque
    together = deque([(i,value) for i,value in enumerate(priorities)])
    cnt = 0
    while True:
        p = together.popleft()
        if any(p[1]<q[1] for q in together):
            together.append(p)
        else:
            cnt +=1
            if p[0]==location:
                return cnt


# print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))