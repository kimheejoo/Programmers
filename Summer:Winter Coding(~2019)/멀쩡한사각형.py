def solution(w,h):
    import math
    return w*h - (w+h-math.gcd(w,h))

print(solution(1,1))