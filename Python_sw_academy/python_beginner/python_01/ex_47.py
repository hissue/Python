'''
가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.

출력
에러발생
'''
number=[]
num=input().split(', ')
sum=0
try:
    number = list(map(int, num))
    for i in number:
        sum = sum + i
    print(sum)

except:
    print('에러발생')
