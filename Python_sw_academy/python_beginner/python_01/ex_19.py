'''
100~300 사이의 숫자에서 각각의 자리숫자가 짝수인 숫자를 찾아
콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.
'''
add = list()
last = list()
for i in range(100, 301):
    a_str = list(str(i))
    a_int = list(map(int, a_str))
    add.append(a_int)
for j in range(len(add)):
    if add[j][0] % 2 == 0 and add[j][1] % 2 == 0 and add[j][2] % 2 == 0:
        last.append(add[j])

for k in range(len(last)):
    for l in range(len(last[k])):
        print(last[k][l], end="")
    if last[k] == last[-1]:
        print("", end="")
    else:
        print(",", end="")


