def solution(prices):
    from collections import deque
    answer = [0]*len(prices)
    prices =deque(prices)
    for idx,_ in enumerate(list(prices)):
        first = prices.popleft()
        for j in prices:
            answer[idx]+=1
            if first>j:
                break
    return answer

print(solution([1,2,3,2,3]))