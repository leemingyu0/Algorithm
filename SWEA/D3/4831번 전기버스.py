import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = [0] + list(map(int, input().split())) + [N]
    cnt = 0
    start = 0
    for i in range(1, M+2):
        if lst[i] - lst[i-1] > K:
            cnt = 0
            break
        if lst[i] - start > K:
            start = lst[i-1]
            cnt += 1
    print(f"#{tc} {cnt}")