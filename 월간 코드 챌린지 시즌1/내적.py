# def solution(a, b):
#     return sum([value*b[idx] for idx, value in enumerate(a)])

def solution(a,b):
    return sum([x*y for x,y in zip(a,b)])

print(solution([-1,0,1],[1,0,-1]))