'''
첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다.

예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다.

단, 비긴 경우는 Result : Draw 라고 출력한다.
'''
rsp = [['바위', '가위'], ['가위', '보'], ['보', '바위']]

Man1 = input()
Man2 = input()
if Man1 == Man2:
    result = 'Result : Draw'
else:
    for i in range(3):
        if Man1 in rsp[i] and Man2 in rsp[i]:
            if Man1 == rsp[i][0]:
                result = 'Result: Man1 Win!'
            else:
                result = 'Result: Man2 Win!'
print(result)

