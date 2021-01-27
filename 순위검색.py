def solution(info, query):
    answer = [0]*len(query)
    info = [i.split() for i in info]
    query = [i.replace(" and",'').split() for i in query]
    for i in range(len(query)):
        for j in info:
            for k in zip(query[i][:-1],j[:-1]):
                if '-' not in k:
                    if k[0] != k[1]:
                        break
            else: 
                if int(query[i][-1]) <= int(j[-1]):
                    answer[i]+=1
        
    return answer

print(solution(["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"], ["java and backend and junior and pizza 100",
                                    "python and frontend and senior and chicken 200",
                                    "cpp and - and senior and pizza 250",
                                    "- and backend and senior and - 150",
                                    "- and - and - and chicken 100",
                                    "- and - and - and - 150"]))