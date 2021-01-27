# def solution(skill, skill_trees):
#     answer = 0
#     for i in skill_trees:
#         tmp = []
#         for j in skill:
#             if j in i:
#                 if tmp:
#                     if tmp[-1] > i.index(j):
#                         break
#                 tmp.append(i.index(j))
#             else:
#                 tmp.append(len(i))
#         else:
#             answer+=1
#     return answer

def solution(skill,skill_trees):
    from collections import deque
    answer = 0
    for i in skill_trees:
        skillList = deque(skill)

        for j in i:
            if j in skill:
                if skillList.popleft() != j: break
        else: answer+=1
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))