'''
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.




A

B

첫 번째 탐색

l=1, r=400, c=200

l=1, r=400, c=200

두 번째 탐색

l=200, r=400, c=300

l=1, r=200, c=100

세 번째 탐색



l=1, r=100, c=50


책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오.
비긴 경우는 0을 출력한다.




[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50


테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000


[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

입력
3
400 300 350
1000 299 578
1000 222 888

출력
#1 A
#2 0
#3 A
'''
T = int(input())
tot=list()
for i in range(T):
    P, Pa, Pb = map(int, input().split())
    h = [Pa, Pb]
    result=list()
    for j in range(len(h)):
        l = 1
        r = P
        c = (l+r) // 2
        count=0
        while True:
            if h[j]==c:
                count=count+1
                result.append(count)
                break

            elif h[j]<c:

                l=l
                r=c
                c = (l + r) // 2
                count=count+1
                continue

            else :
                l=c
                r=r
                c = (l + r) // 2
                count=count+1
                continue

    if result[0]==result[1]:
        tot.append(0)

    elif result[0]<result[1]:
        tot.append('A')

    else :
        tot.append('B')


for i,value in enumerate(tot):
    print('#{} {}'.format(i+1,value))