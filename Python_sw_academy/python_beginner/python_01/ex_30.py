'''어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
입력
11

출력
0 1 2 3 4 5 6 7 8 9

0 2 0 0 0 0 0 0 0 0

'''
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
count = list([0 for _ in range(10)])  # 0으로 초기화
number = list(map(int, input()))

for i in range(len(number)):
    k = number[i]
    count[k] += 1

for l in n:
    print(l, end=" ")
print()
for j in range(len(count)):
    print('{}'.format(count[j]), end=" ")
