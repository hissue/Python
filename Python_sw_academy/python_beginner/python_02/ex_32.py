'''
다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는
프로그램을 작성하십시오.


입력
hello world! 123

출력
LETTERS 10
DIGITS 3
'''
a = input()
len = dict()
st = [i for i in a]
count_st = 0
count_nu = 0
for i in st:
    if 'a' <= i <= 'z':
        count_st += 1

    elif '0' <= i <= '9':
        count_nu += 1
    else:
        continue
len['LETTERS'] = count_st
len['DIGITS'] = count_nu

for i in len.keys():
    print('{} {}'.format(i, len[i]))
