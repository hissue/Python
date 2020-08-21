'''
다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.

입력
2, 3, 4, 5

출력
12.57, 18.85, 25.13, 31.42
'''
import math
n=input()
r=list(map(int,n.split(', ')))
cal_r=list()
result =""
for i in r:
    result+='%0.2f, '%(i*2*math.pi)
print(result[0:-2])


# import math
#
# def dolre(r):
#     dol=r*2*math.pi
#     return dol
#
# from math import pi
# a = input()
# t_list = list(map(int, a.split(', ')))
# result = str()
# for r in t_list:
#    result += "%0.2f, " % (2*pi*r)
#    print(result)
# print(result[0:-2])