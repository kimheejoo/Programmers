# def solution(seoul):
#     x = seoul.index('Kim')
#     return ''.join('김서방은 '+str(x)+'에 있다')

def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(solution(['Kim','Hee','Ju']))