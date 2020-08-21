'''
다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.

입력
abcdefgabc

출력
a,2

b,2

c,2

d,1

e,1

f,1

g,1
'''
w = input()
words = [i for i in w]
d = dict()
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

for key, value in d.items():
    print('{},{}'.format(key, value))
