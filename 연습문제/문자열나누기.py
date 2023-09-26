def solution(s):
    from collections import deque
    answer = 0
    s = deque(s)
    while(s):
        first_num = [s.popleft()]
        if (not s):
            answer += 1
            break
        other_num = []
        while(True):
            next_alpha = s.popleft()
            if(not s):
                answer += 1
                break
            if(next_alpha == first_num[0]):
                first_num.append(next_alpha)
            else:
                other_num.append(next_alpha)
            if(len(first_num) == len(other_num)):
                answer += 1
                break
    return answer

print(solution("abracadabra"))
