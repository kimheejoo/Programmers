def solution(numbers, hand):
    answer = ''
    Left = [10]
    Right = [12]
    for i in numbers:
        if i == 0 : i=11
        if i in [1,4,7]:
            Left.append(i)
            answer+='L'
        elif i in [3,6,9]:
            Right.append(i)
            answer+='R'
        else:
            l1,l2 = divmod(abs(Left[-1] - i), 3)
            r1,r2 = divmod(abs(Right[-1] - i), 3)
            if l1+l2 < r1+r2:
                Left.append(i)
                answer+='L'
            elif l1+l2 == r1+r2:
                if hand=='right':
                    Right.append(i)
                    answer+='R'
                else:
                    Left.append(i)
                    answer+='L'
            else:
                Right.append(i)
                answer+='R'
    return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
print(solution([0,8,2,4,5],'right'))