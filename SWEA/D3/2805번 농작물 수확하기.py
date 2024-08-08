import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    # 중간지점 (가장 긴 지점)
    M = N//2
    # 처음지점 (가장 짧은 지점)
    s, e = M, M
    for i in range(N):
        for j in range(s, e+1):
            ans += arr[i][j]
        if i < M: # 중간지점 이전 지점
            s -= 1
            e += 1
        else: # 중간지점 이후 지점
            s += 1
            e -= 1
    print(f"#{tc} {ans}")