'''다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.'''

he = ["A", "A", "A", "O", "B", "B", "O", "AB", "AB", "O"]
count_a = 0
count_b = 0
count_ab = 0
count_o = 0

for i in range(len(he)):
    if he[i] == "A":
        count_a += 1
    elif he[i] == "B":
        count_b += 1
    elif he[i] == "O":
        count_o += 1
    elif he[i] == "AB":
        count_ab += 1
    else:
        continue

print("{\'A\': %d, \'O\': %d, \'B\': %d, \'AB\': %d}" % (count_a, count_o, count_b, count_ab))
