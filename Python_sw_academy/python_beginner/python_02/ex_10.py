'''
리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.

출력
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)
i=[fibo(i) for i in range(1,11)]
print(i)