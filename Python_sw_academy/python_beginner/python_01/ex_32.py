''' 10진수를 2진수로 변환하는 프로그램을 작성하십시오.'''
a = list()
b = int(input())
while b > 0:
    mok = int(b / 2)
    na = b % 2
    a.append(na)
    b = mok

for i in range(len(a) - 1, -1, -1):
    print(a[i], end='')

