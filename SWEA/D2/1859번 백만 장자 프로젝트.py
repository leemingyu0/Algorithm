import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]
    ans = mx = 0
    for i in lst:
        if mx < i:
            mx = i
        else:
            ans += (mx-i)
    print(f"#{tc} {ans}")