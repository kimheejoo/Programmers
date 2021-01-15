def solution(cacheSize, cities):
    from collections import deque
    answer = 0
    used = deque([])
    if cacheSize==0:
        return len(cities)*5
    cities = [value.lower() for _,value in enumerate(cities)]
    for i in cities:
        if i not in used:
            if len(used) < cacheSize:
                used.append(i)
            else:
                used.popleft()
                used.append(i)
            answer+=5
        else:
            used.remove(i)
            used.append(i)
            answer+=1
    return answer

# print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", 'Jeju', "Pangyo", 'Seoul', 'NewYork', 'LA']))
# print(solution(3,['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
# print(solution(0,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
# print(solution(	2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# print(solution(1,['seiul', 'Seoul']))
