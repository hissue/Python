'''1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.'''
tot = 0
for i in range(1, 101):
    if i % 3 == 0:
        tot += i
    else:
        continue
print('1부터 100사이의 숫자 중 3의 배수의 총합: %d' % tot)

