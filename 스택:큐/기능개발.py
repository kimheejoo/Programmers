def solution(progresses, speeds):
    from collections import deque # 큐
    import math
    answer = deque([]) # 배포하는 데까지 걸리는 날짜 수
    result = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses: # 진행속도를 계산하여 배포하는 데까지 걸리는 날짜 수를 저장
        answer.append(math.ceil((100-progresses.popleft())/(speeds.popleft())))
    cnt = 1
    for _ in list(answer):
        if len(answer):
            a = answer.popleft()
        if not len(answer):
            result.append(cnt)
            break
        for j in list(answer):
            if a >= j: #기준점(맨 왼쪽 수) 보다 작으면 하나씩 pop 하면서 cnt 증가
                answer.popleft()
                cnt+=1
            else: # 큰거 나오면 지금까지의 cnt를 저장하고 중단
                result.append(cnt)
                cnt=1
                break #중단하고 큰 for문으로 가면 answer 맨 왼쪽[0]엔 다음 배포날짜가 나옴
    return result

print(solution([93,30,55],[1,30,5]))
# print(solution([95,90,99,99,80,99],[1,1,1,1,1,1]))
# print(solution([99,99,99,99],[1,3,2,4]))
# print(solution([98],[1]))
# print(solution([99, 1, 99, 1], [1, 1, 1, 1]))