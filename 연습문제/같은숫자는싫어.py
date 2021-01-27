# def solution(arr):
#     answer = []
#     for idx,value in enumerate(arr):
#         if idx==0 or arr[idx]!=arr[idx-1]:
#             answer.append(value)
#     return answer

def solution(arr):
    answer = [value for idx,value in enumerate(arr) if idx==0 or arr[idx]!=arr[idx-1]]
    return answer

print(solution([1,1,3,4,4,4,1,3]))