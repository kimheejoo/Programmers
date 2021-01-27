# def solution(s):
#     answer = True
#     a = 0
#     if len(s)==4 or len(s)==6:
#         for i in s:
#             if i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9':
#                 a = 1
#         if a!=0:
#             answer=False
#     else: answer=False
#     return answer

def solution(s):
    import re
    return bool(re.match('^(\d{4}|\d{6})$',s))

print(solution('a123'))