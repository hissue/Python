'''
다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
팩토리얼 값을 구하는 프로그램을 작성하십시오.

입력
5

출력
120
'''

def recursive(num):
    if num==1:
        tot=1
    else:
         tot = num * recursive(num-1)

    return tot

number = int(input())

print(recursive(number))