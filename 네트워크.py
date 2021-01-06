def solution(n, computers):
    answer = 0
    visited = []
    stack = [0]
    all_stack = set([i for i in range(n)])
    while True:
        if len(visited)==n:
            return answer+1
        if len(stack)==0:
            answer+=1
            stack.append(list(all_stack-set(visited))[0])
        a = stack.pop()
        if a not in visited:
            visited.append(a)
        for j in range(n):
            if computers[a][j]==1 and a!=j and j not in visited:
                stack.append(j)

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))