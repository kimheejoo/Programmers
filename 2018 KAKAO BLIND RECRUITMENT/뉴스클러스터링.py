# def solution(str1, str2):
#     import re
#     list1 = [(str1[i:i+2]).lower() for i in range(len(str1)-1) if re.match('[a-zA-Z]{2}',str1[i:i+2])]
#     list2 = [(str2[i:i+2]).lower() for i in range(len(str2)-1) if re.match('[a-zA-Z]{2}',str2[i:i+2])]
#     gyo = 0
#     if not list1 and not list2: return 65536
#     for i in list1:
#         if i in list2:
#             gyo+=1
#             list2[list2.index(i)] = '$$$'
#     hap = len(list1+list2)-gyo
#     return int((gyo/hap)*65536)

def solution(str1,str2):
    import re
    list1 = [(str1[i:i+2]).lower() for i in range(len(str1)-1) if re.match('[a-zA-Z]{2}',str1[i:i+2])]
    list2 = [(str2[i:i+2]).lower() for i in range(len(str2)-1) if re.match('[a-zA-Z]{2}',str2[i:i+2])]
    
    if not list1 and not list2: return 65536

    gyo = set(list1) & set(list2)
    hap = set(list1) | set(list2)

    _gyo = sum([min(list1.count(g), list2.count(g)) for g in gyo])
    _hap = sum([max(list1.count(h), list2.count(h)) for h in hap])
    return int(_gyo/_hap*65536)


    
print(solution("FRANCE","french"))
# print(solution("handshake","shake hands"))
# print(solution("aa1+aa2","AAAA12"))
# print(solution("E=M*C^2","e=m*c^2"))
# print(solution("Aaaaa","aaab"))
# print(solution("aaabbbc","aabbdf"))
# print(solution("AA","BB"))
# print(solution("ab ab","ab cd"))