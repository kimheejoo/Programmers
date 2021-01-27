def solution(record):
    answer = []
    person = {}
    for i in record:
        rec = i.split()
        if len(rec)==3:
            person[rec[1]]=rec[2]

    for i in record:
        rec = i.split()
        if rec[0]=='Enter':
            answer.append(person[rec[1]]+'님이 들어왔습니다.')
        elif rec[0]=='Leave':
            answer.append(person[rec[1]]+'님이 나갔습니다.')
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))