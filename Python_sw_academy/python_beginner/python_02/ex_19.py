'''
주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.

출력
(1, 2, 3, 4, 5)
(6, 7, 8, 9, 10)
'''
num=(1,2,3,4,5,6,7,8,9,10)
l_num=list(num)
a=list()
k=list()
count=0
for i in l_num:
    a.append(i)
    count += 1
    if count==len(l_num)/2:
        k.append(a)
        a = []
        count = 0
a_tu=list(map(tuple,k))
for i in range(2):
    print(a_tu[i])

