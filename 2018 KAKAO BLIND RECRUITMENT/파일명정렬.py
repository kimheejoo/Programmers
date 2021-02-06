def solution(files):
    import re
    answer = [[i,re.findall('([a-zA-Z ]+[-. ]?)(\d+)',files[i].lower())] for i in range(len(files))]
    answer.sort(key= lambda x:(x[1][0][0],int(x[1][0][1])))
    result = []
    for i in answer:
        result.append(files[i[0]])
    return result

print(solution(['img12a1.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
# print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))