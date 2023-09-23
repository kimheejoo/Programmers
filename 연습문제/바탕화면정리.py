def solution(wallpaper):
    answer = [len(wallpaper)-1, len(wallpaper[0])-1, -1, -1]
    for (index, wall) in enumerate(wallpaper):
        if ('#' in wall):
            answer[0] = min(answer[0], index)
            answer[2] = max(answer[2], index + 1)
            for (index, sharp) in enumerate(wall):
                if (sharp == '#'):
                    answer[1] = min(answer[1], index)
                    answer[3] = max(answer[3], index + 1)
    return answer

print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))