'''
인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때,
칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.




예를 들어 2개의 색칠 영역을 갖는 색칠 정보이다.

2

2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )

3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )



[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강), color = 2 (파랑)



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



입력
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

출력
#1 4
#2 5
#3 7
'''
n = 10
T = int(input())
result=list()
for i in range(T):
    arr = [[0] * n for _ in range(n)]
    N = int(input())
    lists=list()
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        lists.append([r1, c1, r2, c2, color])

    count=0
    c=0
    while True:
        for i in range(0,N):
            if lists[i][4] == 1:
                c=c+1
                first1 = lists[i][0]
                end1 = lists[i][2] + 1
                first2 = lists[i][1]
                end2 = lists[i][3] + 1
                for k in range(first1, end1):
                    for m in range(first2, end2):
                        if arr[k][m] == 2:
                            count=count+1
                        else: arr[k][m] = 1



            else:
                c=c+1
                first1 = lists[i][0]
                end1 = lists[i][2] + 1
                first2 = lists[i][1]
                end2 = lists[i][3] + 1
                for k in range(first1, end1):
                    for m in range(first2, end2):
                        if arr[k][m] == 1:
                            count=count+1
                        arr[k][m] = 2


        if c==N:
            result.append(count)
            break

for i,value in enumerate(result):
    print('#{} {}'.format(i+1,value))







