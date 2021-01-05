answer = 0
def DFS(idx, numbers, target, value):
    global answer
    if idx == len(numbers):
        if value == target:
            answer+=1
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
    


def solution(numbers, target):
    DFS(0,numbers,target,0)
    return answer

print(solution([1,1,1,1,1],3))