def solution(expression):
    from itertools import permutations
    import re
    maxNum = -1
    number = list(map(int, re.findall('\d+', expression)))
    operator = re.findall('[-*+]', expression)
    priority = permutations(set(operator),len(set(operator)))
    for i in priority:
        number_ = number[:]
        operator_ = operator[:]
        for now in i:
            j = 0
            while True:
                if j == len(operator_): break
                tmp = 0
                if now == operator_[j]:
                    if now == '-':
                        tmp += number_[j] - number_[j+1]
                    elif now == '+':
                        tmp += number_[j] + number_[j+1]
                    else:
                        tmp += number_[j] * number_[j+1]
                    number_.pop(j+1)
                    number_.pop(j)
                    number_.insert(j,tmp)
                    operator_.pop(j)
                else: j+=1
        maxNum = max(maxNum, abs(number_[0]))
    return maxNum

print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))