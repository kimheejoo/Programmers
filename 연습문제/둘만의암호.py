def solution(s, skip, index):
    answer = ''
    for alpha in s:
        tmp = ord(alpha) - ord('a')
        idx = index
        while(idx):
            tmp = (tmp + 1) % 26
            if (chr(tmp + ord('a')) not in skip):
                idx -= 1      
        answer+=chr(tmp + ord('a'))
    return answer

print(solution("aukks", "wbqd", 5))