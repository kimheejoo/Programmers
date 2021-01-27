def solution(s):
    mini = len(s)
    s = [''.join(list(i)) for i in s]
    for i in range(1,len(s)+1):
        ans = ''
        cnt = 1
        for idx in range(0,len(s),i):
            now = ''.join(s[idx:idx+i])
            if s[idx:idx+i]==s[idx+i:idx+i+i]:
                cnt += 1
                continue
            else:
                if cnt > 1:
                    ans += str(cnt)
                    cnt = 1
                ans += now
        mini = min(mini,len(ans))
    return mini

# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))