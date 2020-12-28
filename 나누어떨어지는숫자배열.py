# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i%divisor==0:
#             answer.append(i)
#     if len(answer)==0:
#         answer.append(-1)
#     return sorted(answer)

def solution(arr, divisor):
    return sorted([i for i in arr if i%divisor==0]) or [-1]

print(solution([5,9,7,10],6))