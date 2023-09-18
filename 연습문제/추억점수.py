def solution(name, yearning, photo):
    answer = []
    nameYearning = {}
    for i in range(len(name)):
        nameYearning[name[i]] = yearning[i]
    
    for i in photo:
        tmp = 0
        for j in i:
            if j in nameYearning.keys():
                tmp += nameYearning[j]
        answer.append(tmp)
            
    return answer