def solution(keymap, targets):
    answer = [0] * len(targets)
    keyDict = {}
    for key in keymap:
        for (index, alpha) in enumerate(key):
            if (alpha not in keyDict.keys()):
                keyDict[alpha] = index + 1
            else:
                keyDict[alpha] = min(keyDict[alpha], index + 1)
    
    for (index, target) in enumerate(targets):
        sumValue = 0
        for alpha in target:
            if (alpha in keyDict.keys()):
                sumValue += keyDict[alpha]
            else:
                answer[index] = -1
                sumValue = 0
                break
        if (sumValue): answer[index] += sumValue
    
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))