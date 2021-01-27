def solution(m, n, board):
    from collections import deque
    answer = 0
    board = [list(i) for i in board]
    
    while True:
        flag = 0
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!='_' and board[i][j].upper() == board[i][j+1].upper() == board[i+1][j].upper() == board[i+1][j+1].upper():
                    board[i][j] = board[i][j].lower()
                    board[i][j+1] = board[i][j+1].lower()
                    board[i+1][j] = board[i+1][j].lower()
                    board[i+1][j+1] = board[i+1][j+1].lower()
                    flag = 1
        
        if flag == 0: return answer
        
        for j in range(n):
            cnt = 0
            lower = deque()
            upper = deque()
            for i in range(m):
                if board[i][j].islower():
                    board[i][j] = '_'
                    lower.append(board[i][j])
                    cnt+=1
                else:
                    upper.append(board[i][j])
            
            index = 0
            while lower:
                board[index][j] = lower.popleft()
                index+=1
            while upper:
                board[index][j] = upper.popleft()
                index+=1
            
            answer += cnt

# print(solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6,6,['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))