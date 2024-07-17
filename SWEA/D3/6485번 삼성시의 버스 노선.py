import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = [0] * 5000
    N = int(input())
    for  _ in range(N):
        A, B = map(int, input().split())
        for i in range(A-1, B):
            lst[i] += 1
    P = int(input())
    ans = []
    for _ in range(P):
        ans.append(lst[int(input())-1])
    print(f"#{tc}", *ans)