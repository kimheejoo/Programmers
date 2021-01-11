# def solution(s):
#     answer = []
#     s = sorted(s[2:-2].split("},{"), key=lambda x: len(x))
#     if len(s)==1:
#         return list(map(int, s))
#     for i in range(len(s)-1):
#         if i==0: answer.append(s[i])
#         answer.append(''.join(set(s[i+1].split(",")) - set(s[i].split(','))))
#     return list(map(int,answer))

def solution(s):
    import re
    from collections import Counter
    return list(map(int, [i for i, v in sorted(Counter(re.findall('\d+',s)).items(), key=lambda x: x[1],reverse=True)]))

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{123,20},{20}}"))
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))