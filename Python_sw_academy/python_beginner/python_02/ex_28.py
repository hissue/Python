'''
아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성하십시오.
"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000,

출력
TV: 2000000
냉장고: 1500000
노트북: 1200000
세탁기: 1000000
책상: 350000
가스레인지: 200000

'''
b=[]
mur={"TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}
a=[i for i in mur.items()]
mur.clear()
c=[]

for key,value in a:
    a=(value,key)
    b.append(a)
b.sort(reverse=True)

for value,key in b:
    b=(key,value)
    c.append(b)
for key,value in c:
    print('{}: {}'.format(key,value))



