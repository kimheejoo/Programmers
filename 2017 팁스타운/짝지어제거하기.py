def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] == i:
            stack.pop()
        else: stack.append(i)
    if stack: return 0
    else: return 1
        

print(solution('baabaa'))
print(solution('cdcd'))