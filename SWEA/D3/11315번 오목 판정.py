import sys
sys.stdin = open("input.txt", "r")

di = [0, 1, 1, 1]
dj = [1, 0, 1, -1]

def solve():
    for si in range(N):
        for sj in range(N):
            for dr in range(4):
                for mul in range(5):
                    ni = si + di[dr] * mul
                    nj = sj + dj[dr] * mul
                    # 범위 이내이며  o가 5개 연속인지 판별
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        # 이어서 다음 것도 o인지 찾기
                        pass
                    else:
                        # 더 볼 필요도 없으므로 break
                        break
                else:
                    return "YES"
    return "NO"
            
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = solve()
    print(f"#{tc} {ans}")