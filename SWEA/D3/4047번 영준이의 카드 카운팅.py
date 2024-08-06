import sys
sys.stdin = open("input.txt", "r")

dic = {'S':0, 'D':1, 'H':2, 'C':3}
T = int(input())
for tc in range(1, T+1):
    st = input()
    arr = [[] for _ in range(4)]

    #빈 arr에 뽑은 숫자 추가
    for i in range(0, len(st), 3):
        arr[dic[st[i]]].append(int(st[i+1:i+3]))

    ans = []
    for lst in arr:
        # set으로 중복제거해서 갯수 비교로 중복하는 것 있나 체크
        if len(lst) != len(set(lst)):
            print(f"#{tc} ERROR")
            break
        ans.append(13-len(lst))
    else:
        print(f"#{tc}", *ans)