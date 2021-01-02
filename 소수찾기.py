def is_prime(n):
    if n<2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    else: return True

def solution(numbers):
    from itertools import permutations
    answer = 0
    result = []
    for i in range(len(numbers)):
        result += set(map(int, map(''.join, permutations(numbers, i+1))))
    for i in set(result):
        if is_prime(i): answer+=1
    return answer

print(solution('011'))