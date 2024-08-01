import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 200 # 공유하는 복도 수
    for _ in range(N):
        s, e = map(int, input().split())
        # 예외 상황 정렬
        if s > e:
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2+1):
            cnt[i] += 1
    print(f"#{tc} {max(cnt)}")