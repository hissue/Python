'''1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.
 '''
odd=list()
for i in range(1,101):
    if i%2==1:
        odd.append(i)
for j in range(len(odd)):
    if odd[j]==odd[-1]:
            print(odd[j],end=" ")
    else :
            print(odd[j],end=", ")
