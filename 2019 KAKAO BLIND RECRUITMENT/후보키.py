def solution(relation):
    from itertools import combinations
    tupleNum = len(relation) #6
    attributeNum = len(relation[0]) #3
    relation = list(map(list, zip(*relation)))
    result = []
    for i in range(attributeNum):
        allCombi = combinations(range(attributeNum),i+1)
        for j in allCombi:
            tmp = []
            for k in j:
                tmp.append(relation[k])
            if len(set(zip(*tmp))) == tupleNum:
                for ret in result:
                    if set(ret).issubset(set(j)):
                        break
                else:
                    result.append(j)
    return len(result)

print(solution(
[["100","ryan","music"],["200","apeach","math"],
["300","tube","computer"],["400","con","computer"],
["500","muzi","music"],["600","apeach","music"]]
))