def solution(orders, course):
    from itertools import combinations
    answer = []
    for i in course:
        dic = {}
        for j in orders:
            for s in combinations(sorted(j),i):
                if ''.join(s) in dic.keys(): dic[''.join(s)] +=1
                else: dic[''.join(s)] = 1
        if not dic: continue
        maxNum = max(dic.items(), key = lambda x:x[1])[1]
        for x in dic.items():
            if x[1]==maxNum and maxNum>=2:
                answer.append(x[0])
    return sorted(answer)

# def solution(orders, course):
#     from itertools import combinations
#     from collections import Counter
#     answer = []
#     for i in course:
#         dic = []
#         for j in orders:
#             for s in combinations(sorted(j),i):
#                 dic.append(''.join(s))
#         dic = Counter(dic).most_common()
#         maxNum = dic[0][1]
#         for x in dic:
#             if x[1]==maxNum and maxNum>=2:
#                 answer.append(x[0])
#     return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))