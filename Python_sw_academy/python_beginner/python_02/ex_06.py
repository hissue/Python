'''
리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.

입력
10
10
20
30
40

출력
입력된 값 [10, 10, 20, 30, 40]의 평균은 22.0입니다.
'''

num=[input() for i in range(5)]
# for i in range(5):
#     num.append(input())
k=list(map(int,num))
print('입력된 값 {0}의 평균은 {1:0.1F}입니다.'.format(k,sum(k)/5))