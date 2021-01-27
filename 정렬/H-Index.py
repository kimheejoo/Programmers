def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i]<=i+1:
            return i
    return len(citations)

# print(solution([10,11,12,13]))
print(solution([25,8,5,3,3]))