def tenToWhat(num,what):
    result = []
    remain = ['A','B','C','D','E','F']
    while num:
        num, namaji = divmod(num,what)
        if namaji>=10:
            namaji-=10
            result.append(remain[namaji])
        else: result.append(str(namaji))
    return ''.join(result[::-1])

def solution(n, t, m, p):
    num = 1
    tmp = '0'
    while True:
        if len(tmp)>t*m:
            break
        tmp+= tenToWhat(num, n)
        num+=1
    answer = tmp[p-1::m][:t]
    # answer = [tmp[i] for i in range(len(tmp)) if i%m==p-1]
    return ''.join(answer)
    
# print(solution(2,4,2,1))
print(solution(16,16,2,1))