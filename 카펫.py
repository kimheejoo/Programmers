def solution(brown, yellow):
    s = brown+yellow
    for i in range(s,0,-1):
        if s%i==0:
            if (i-2)*(s/i-2)==yellow:
                return [i,s//i]


print(solution(10,2))
print(solution(8,1))
print(solution(24,24))