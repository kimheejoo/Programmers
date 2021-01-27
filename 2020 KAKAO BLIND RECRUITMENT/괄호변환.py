def two(v):
    # open_b = []
    # close_b = []
    # for i in range(len(v)):
    #     if v[i]=='(':
    #         open_b.append(v[i])
    #     else:
    #         close_b.append(v[i])
    #     if len(open_b) == len(close_b):
    #         ru = v[:i+1]
    #         rv = v[i+1:]
    #         return ru,rv
    c = 0
    for i in range(len(v)):
        if v[i]=='(': c+=1
        else: c-=1
        if c == 0 :
            return v[:i+1], v[i+1:]
            
def right(u):
    # open_b = []
    # u = [i for i in u]
    # for i in u:
    #     if i == ')':
    #         if not open_b:
    #             return False
    #         open_b.pop()
    #     else:
    #         open_b.append(i)
    # if not open_b:
    #     return True
    c = 0
    for i in u:
        if i=='(': c+=1
        else: c-=1
        if c < 0: return False
    if c == 0: return True



def solution(w):
    if w=='':
        return w
    u, v = two(w)
    if right(u):
        return u + solution(v)
    else:
        ret = '(' + solution(v)+')'
        # u = [i for i in u[1:-1]]
        ret += ''.join(list(map(lambda x: '(' if x==')' else ')',u[1:-1])))
        # for i in range(len(u)):
        #     if u[i]=='(': u[i]=')'
        #     else: u[i]='('            
        # ret += ''.join(u)
        return ret

# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))