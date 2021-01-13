def solution(n, arr1, arr2):
    return [j.replace('1','#').replace('0',' ') for j in [bin(arr1[i]|arr2[i])[2:].zfill(n) for i in range(n)]]
        


print(solution(5,[9,1,28,18,11],[30,1,21,17,28]))
# print(solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10]))