'''
다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는
프로그램을 작성하십시오.

입력
H1e2l3l4o5w6o7r8l9d

출력
Helloworld
'''

s=input()
st=[i for i in s]
for i in range(len(st)):
    if i%2==0:
        print('{}'.format(st[i]),end='')
