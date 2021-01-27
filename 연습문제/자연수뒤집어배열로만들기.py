# def solution(n):
#     return [int(i) for i in (list(str(n)))[::-1]]

def solution(n):
    return list(map(int, reversed(str(n))))

print(solution(12345))