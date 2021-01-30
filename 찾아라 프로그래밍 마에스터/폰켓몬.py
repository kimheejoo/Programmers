# def solution(nums):
#     leng = len(nums)//2
#     nums = set(nums)
#     if len(nums)<leng:
#         return len(nums)
#     return leng

def solution(nums):
    return min(len(set(nums)),len(nums)//2)



print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,2]))