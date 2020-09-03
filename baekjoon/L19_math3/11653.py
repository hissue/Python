'''
입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다.

예제 입력 1
72
예제 출력 1
2
2
2
3
3
예제 입력 2
3
예제 출력 2
3
예제 입력 3
6
예제 출력 3
2
3
예제 입력 4
2
예제 출력 4
2
예제 입력 5
9991
예제 출력 5
97
103
'''
v = int(input())
i=2
while v!=1 :
    if v%i == 0:
        v = v/i
        print(i)
    else : i+=1


# def solution(n):
#     primes=[]
#     a=[False,False]+[True]*(n-1)
#     for i in range(2,n+1):
#         if a[i]:
#             primes.append(i)
#             for j in range(2*i,n+1,i):
#                 a[j]=False
#     return primes
# n=int(input())
# primes=solution(n)
# i=0
# result=[]
# while True:
#     if n%primes[i]==0:
#         result.append(primes[i])
#         n=n//primes[i]
#     else:
#         i+=1
#     if n in primes:
#         result.append(n)
#         break
# for i in result:
#     print(i)

