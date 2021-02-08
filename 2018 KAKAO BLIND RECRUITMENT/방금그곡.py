def solution(m, musicinfos):
    import re
    answer = ''
    maxTime = 0
    for i in musicinfos:
        tmp = i.split(',')
        runningTime = (int(tmp[1].split(':')[0]) - int(tmp[0].split(':')[0]))*60 + (int(tmp[1].split(':')[1]) - int(tmp[0].split(':')[1]))
        mok, namaji = divmod(runningTime, len(tmp[3]))
        if m in tmp[3]*mok+tmp[3][:namaji]:
            if not m+'#' in tmp[3]*mok+tmp[3][:namaji]:
                if maxTime < runningTime:
                    maxTime = runningTime
                    answer = tmp[2]

    return answer

# print(solution('ABCDEFG',['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
print(solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))