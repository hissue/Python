'''
다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는
프로그램을 작성하십시오.


입력
Hello World! 123

출력
UPPER CASE 2
LOWER CASE 8
'''
a=input()
le=dict()
st=[i for i in a]
count_up=0
count_lo=0
for i in st:
    if 'A'<=i<='Z':
        count_up+=1
    elif 'a'<=i<='z':
        count_lo+=1
    else:
        continue
le['UPPER CASE']=count_up
le['LOWER CASE']=count_lo

for key,value in le.items():
    print('{} {}'.format(key,value))
