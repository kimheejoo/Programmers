# def solution(s):
#     result = []
#     for i in s.split(' '):
#         a = ''
#         for idx,j in enumerate(i):
#             if idx%2==0: a += j.upper()
#             else: a += j.lower()
#         result.append(a)
#     return ' '.join(result)

def solution(s):
    return ' '.join([''.join([j.upper() if idx%2==0 else j.lower() for idx,j in enumerate(i)]) for i in s.split(' ')])    
print(solution('try hello world'))