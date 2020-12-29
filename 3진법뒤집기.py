def solution(n):
    ans = []
    while(n):
        n,b = divmod(n,3)
        ans.append(b)
    answer = sum([value*(3**i) for i,value in enumerate(list(reversed(ans)))])
    return answer

print(solution(125))