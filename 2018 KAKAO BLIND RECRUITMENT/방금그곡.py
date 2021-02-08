def solution(m, musicinfos):
    answer = ''
    maxTime = 0
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    for i in musicinfos:
        tmp = i.split(',')
        runningTime = (int(tmp[1].split(':')[0]) - int(tmp[0].split(':')[0]))*60 + (int(tmp[1].split(':')[1]) - int(tmp[0].split(':')[1]))
        tmp[3] = tmp[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        mok, namaji = divmod(runningTime, len(tmp[3]))
        music = tmp[3]*mok+tmp[3][:namaji]
        if m in music:
            if maxTime < runningTime:
                maxTime = runningTime
                answer = tmp[2]
    # if answer: return answer
    # else: return "(None)"
    return answer if answer else "(None)"

# print(solution('ABCDEFG',['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
print(solution('Aaa', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))