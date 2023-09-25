def solution(today, terms, privacies):
    answer = []
    new_terms = {}
    for term in terms:
        new_terms[term.split(' ')[0]] = int(term.split(' ')[1])
        
    for (index, privacy) in enumerate(privacies):
        period = privacy.split(' ')[0].split('.')
        term = privacy.split(' ')[1]
        year, month, date = int(period[0]), int(period[1]), period[2]

        year = year + int((month + new_terms[term] -1) / 12)
        month = (month + new_terms[term] -1) % 12 + 1
        if('.'.join([str(year), f'{month:02d}', date]) <= today):
            answer.append(index + 1)
        
    return answer

print(solution(	
    "2020.01.01", ["Z 3", "D 5"], 
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))