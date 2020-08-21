'''다음은 학생의 점수를 나타내는 리스트입니다.

[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.'''

index=list()
score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
tot=0

for i in range(len(score)):
    if score[i] < 80:
        index.append(i)
    else:
        continue

for j in range(len(index)):
    score.pop(index[j])
    for k in range(len(index)):
        index[k]=index[k]-1
for i in score:
    tot+=i
print(tot)
