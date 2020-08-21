'''
리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.

출력
[1, 2, 3, 4, 3, 2, 1]
[1, 2, 3, 4]
'''

def arr_l(no_arr):
    y_arr=list(set(no_arr))
    return y_arr

l=[1,2,3,4,3,2,1]
arrange_l=arr_l(l)
print(arrange_l)
