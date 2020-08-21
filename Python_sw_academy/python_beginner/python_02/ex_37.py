'''
다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는
코드를 작성하십시오.


입력
madam

출력
madam
입력하신 단어는 회문(Palindrome)입니다.
'''


def i_st(s, count):
    if cir[s] == cir[-s - 1]:
        count += 1
        return count
    else:
        return


cir = input()
count = 0
cir_len = len(cir) // 2
for j in range(0, cir_len):
    count = i_st(j, count)
if count == cir_len:
    print(cir)
    print('입력하신 단어는 회문(Palindrome)입니다.')


