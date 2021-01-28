def solution(nums):
    from itertools import combinations
    answer = 0
    hubo = combinations(nums,3)
    for i in [sum(i) for i in hubo]:
        for j in range(2,i):
            if i%j == 0:break
        else: answer+=1
    return answer

# print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))