# def solution(strings, n):
#     answer = []
#     a = sorted([i[n] for i in strings],reverse=False)
#     strings = sorted(strings,reverse=False)
#     s = [1]*len(strings)
#     for i in a: #c c x
#         for idx,j in enumerate(strings): # abcd abce cdx
#             if j[n]==i and s[idx]==1:
#                 answer.append(j)
#                 s[idx] = 0
#                 break
#     return answer

def solution(strings, n):
    return sorted(sorted(strings), key = lambda x:x[n])

print(solution(['sun', 'bed', 'car'],1))
print(solution(['abce', 'abcd', 'cdx'],2))