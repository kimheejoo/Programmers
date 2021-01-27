# def solution(n):
#     answer = 0
#     result = []
#     while n:
#         n,i = divmod(n,10)
#         result.append(i)
#     answer = sum([i*(10**idx) for idx,i in enumerate(sorted(result))])
#     return answer

def solution(n):
    return ''.join(sorted(list(str(n)),reverse=True))

print(solution(118372))