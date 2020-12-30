def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    result = [0,0,0]
    for idx, value in enumerate(answers):
        if one[idx%len(one)]==value:
            result[0]+=1
        if two[idx%len(two)] == value:
            result[1]+=1
        if three[idx%len(three)] == value:
            result[2]+=1
    answer = [idx+1 for idx,i in enumerate(result) if i==max(result)]
    return answer

print(solution([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]))