import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    _ = input()
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # 사다리의 처음이아닌 마지막에서 2를 찾고
    # 거꾸로 위로 올라가는 풀이법
    ci = 99
    for i in range(102):
        if arr[ci][i] == 2:
            cj = i
    
    # 사다리의 맨 위로 올라갈 때까지 진행
    while ci > 0:
        arr[ci][cj] = 0    # 지나간 자리는 0으로 지우기
        if arr[ci][cj + 1] == 1:    # 오른쪽이 1
            cj += 1
        elif arr[ci][cj - 1] == 1:  # 왼쪽이 1
            cj -= 1
        else:   # 위에만 1
            ci -= 1
    print(f"#{tc} {cj-1}")