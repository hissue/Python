'''
결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
입력
10

출력
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''
def fibo(fir,sec,ra):
    update_n = 0
    temp=[fir,sec]
    for i in range(ra-2):
        update_n = fir + sec
        fir = sec
        sec = update_n
        temp.append(update_n)
    return temp

i= int(input())
a=1
b=1
fibonaci=fibo(a,b,i)
print(fibonaci)


