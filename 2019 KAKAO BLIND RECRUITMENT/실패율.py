def solution(N, stages):
    answer = []
    stages.sort()
    for i in range(1,N+1):
        c = stages.count(i)
        if len(stages): answer.append((i,c/len(stages)))
        else: answer.append((i,0))
        stages = stages[c:]
    return [i[0] for i in sorted(answer,key=lambda x: x[1], reverse=True)]

# print(solution(5,[2,1,2,6,2,4,3,3]))
# print(solution(4,[4,4,4,4,4]))
print(solution(4,[1,1,1,1]))