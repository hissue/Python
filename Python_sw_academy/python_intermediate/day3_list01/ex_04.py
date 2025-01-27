'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을
하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수
식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.


10 1 9 2 8 3 7 4 6 5


주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오



[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다.
10<=N<=100, 1<=ai<=100



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를
10개까지 출력한다.

입력
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

출력
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21
'''

T = int(input())
result = list()
for i in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    ai = sorted(ai)
    ai_f = list()
    ai_s = list()
    k = 0
    for i in ai:
        k = k + 1
        if k <= len(ai) / 2:
            ai_f.append(i)
        else:
            ai_s.append(i)
    ai_s = sorted(ai_s, reverse=True)
    ai = list(zip(ai_s, ai_f))
    ai = [list(i) for i in ai]
    result.append(sum(ai, []))
m = 1
for j in range(T):
    print('#{}'.format(m), end=' ')
    for i in range(10):
        print('{}'.format(result[j][i]), end=' ')
    m = m + 1
    print()
