import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    mx = 0
    mn = 9999999
    for si in range(N-M+1):
        sm = 0
        for i in range(si, si+M):
            sm += lst[i]
        if  sm > mx:
            mx = sm
        if  sm < mn:
            mn = sm
    print(f"#{tc} {mx-mn}")