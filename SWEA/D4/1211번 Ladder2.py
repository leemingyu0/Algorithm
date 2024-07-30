import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    mn = 100*100
    for sj in range(1, 101):
        # ci == 0, sj == 1 이라면 출발
        if arr[0][sj] == 0:
            continue
        cj = sj
        cnt = dr = ci = 0
        while ci < 99:
            cnt += 1
            # 방향전환
            # dr = 0 : 하
            # dr = -1 : 좌
            # dr = 1 : 우
            if dr == 0: 
                ci += 1    # 이동
                if arr[ci][cj-1] == 1:
                    dr = -1
                elif arr[ci][cj+1] == 1:
                    dr = 1
            else:
                cj += dr    # 이동
                if arr[ci][cj+dr] == 0:
                    dr = 0
        if mn >= cnt:
            mn, ans = cnt, sj - 1
    print(f"#{tc} {ans}")