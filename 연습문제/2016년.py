# def solution(a, b):
#     month = [31,29,31,30,31,30,31,31,30,31,30,31]
#     dayOfWeek = ['MON','TUE','WED','THU','FRI','SAT','SUN']
#     day = (sum([month[i] for i in range(a-1)])+b)%7-1
#     return dayOfWeek[(4+day)%7]

def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    dayOfWeek = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    day = (sum(month[:a-1])+b)%7-1
    return dayOfWeek[(4+day)%7]

print(solution(5,24))