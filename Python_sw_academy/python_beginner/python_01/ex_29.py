'''
while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
*******

 *****

  ***

   *
'''
i = 7
k = 0
while i >= 0:
    print(' ' * k, '*' * i)
    i = i - 2
    k = k + 1



