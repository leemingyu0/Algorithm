import sys
sys.stdin = open("input.txt", "r")

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    
    # 초기화
    i, j, cnt, dr = 0, 0, 1, 0
    arr[i][j] = cnt
    cnt += 1
    
    while cnt <= N * N:
        ni = i + di[dr]
        nj = j + dj[dr]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr + 1) % 4
    
    print(f"#{tc}")
    for lst in arr:
        print(*lst)