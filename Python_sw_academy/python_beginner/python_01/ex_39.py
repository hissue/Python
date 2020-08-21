'''
정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
'''
def num(number,lsit_value):

    for i in number:
        if i in lsit_value:
            print('%d => True'%i)
        else :
            print('%d => False'%i)


list=[2,4,6,8,10]
number=[5,10]
print(list)
num(number,list)

