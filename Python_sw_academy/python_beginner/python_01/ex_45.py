'''
다음의 결과와 같이 이름과 나이를 입력 받아
올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.

입력
홍길동
20

출력
홍길동(은)는 2099년에 100세가 될 것입니다.
'''
import datetime

def date(my_age):
    day = datetime.datetime.now()
    now_year = day.year
    return calcurate(now_year,my_age)

def calcurate(now_y,_age):
    rest=100-_age-1
    final=now_y+rest
    return final

name = input()
age = int(input())

now=date(age)

print('{}(은)는 {}년에 100세가 될 것입니다.'.format(name,now))