def solution(n):
    water = ['수','박']
    return ''.join([water[i%2] for i in range(n)])
    

print(solution(5))