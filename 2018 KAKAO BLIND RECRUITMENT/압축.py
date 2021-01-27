def solution(msg):
    # di = dict()
    answer = []
    k = 26
    # for i in range(k):
    #     di[chr(65+i)] = i+1
    di = {chr(65+i):i+1 for i in range(k)}
    i = 0
    while True:
        tmp = ''
        for j in range(i,len(msg)):
            if msg[i:j+1] in di.keys():
                tmp = msg[i:j+1]
            else:
                di[msg[i:j+1]] = k+1
                k+=1
                answer.append(di[tmp])
                i += len(tmp)
                break
        else:
            answer.append(di[tmp])
            break
    return answer

# print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))