import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    for i in range(N):
        lst[0] += 1
        lst[-1] -= 1
        lst.sort()
    print(f"#{tc} {lst[-1] - lst[0]}")