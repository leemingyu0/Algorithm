import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        # 우선 첫번째 층이 최대라고 가정하고
        mx = lst[i-2]
        # 첫번째 층 제외하고 나머지 반복문 순회하면서
        for si in range(i-1, i+3):
            # 자신인 경우 예외처리
            if i == si:
                continue
            # 자신을 제외한 최대의 층 수 계산
            if lst[si] > mx:
                mx = lst[si]
        # 우리 집보다 자신을 제외한 최대의 층의 차이를 더하기
        if lst[i] >= mx:
            cnt += lst[i] - mx
    print(f"#{tc} {cnt}")