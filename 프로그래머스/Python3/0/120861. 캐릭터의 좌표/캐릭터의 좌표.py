def solution(keyinput, board):
    answer = []
    x0, y0 = 0, 0
    a, b  = 0, 0
    x, y = board
    w, l = int((x - 1) / 2), int((y - 1) / 2)
    direction = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    for i in keyinput:
        a += direction[i][0]
        b += direction[i][1]
        if -w <= a <= w and -l <= b <= l:
            print(b)
            x0 += direction[i][0]
            y0 += direction[i][1]
        else:
            a -= direction[i][0]
            b -= direction[i][1]
    answer.append(x0)
    answer.append(y0)
    return answer