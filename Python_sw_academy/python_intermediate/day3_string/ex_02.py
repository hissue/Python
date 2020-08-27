'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서
길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ

출력
#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT
'''

def nm_equal(N, M, temp):
    arr_garo = list()
    arr_sero = list()
    for i in range(N):
        a = [temp[i][j] for j in range(M)]
        arr_garo.insert(0, ''.join(a))
    for i in range(M):
        b = [temp[j][i] for j in range(N)]
        arr_sero.insert(0, ''.join(b))
    for k in range(N):
        if arr_garo[k] == ''.join(reversed(arr_garo[k])):
            return arr_garo[k]

        elif arr_sero[k] == ''.join(reversed(arr_sero[k])):
            return arr_sero[k]

        else:
            continue


def nm_diff(N, M, temp):
    arr_garo = list()
    arr_sero = list()
    for l in range(N):
        for i in range(N-M+1):
            arr_garo.append(''.join(temp[l][i:M + i]))

    #         arr_sero.append(''.join(temp[i:M][l]))
    # print(arr_garo)
    for k in range(N*(N-M+1)):
        if arr_garo[k] == ''.join(list(reversed(arr_garo[k]))):
            return arr_garo[k]
        # elif arr_sero[k] == ''.join(list(reversed(arr_sero[k]))):
        #     return arr_sero[k]
        # else:
        #     continue


T=int(input())
a = list()
i = 0
result = list()
for t in range(T):  # T
    N, M = map(int, input().split())
    temp = list()

    for l in range(N):
        temp.append(list(input()))

    if N == M:
        result.append(nm_equal(N, M, temp))

    else:
        result.append(nm_diff(N, M, temp))

for i,value in enumerate(result):
    print('#{} {}'.format(i+1,value))

print(temp)



# def nm_equal(N, M, temp):
#     arr_garo = list()
#     arr_sero = list()
#     for i in range(N):
#         a = [temp[i][j] for j in range(M)]
#         arr_garo.insert(0, ''.join(a))
#     for i in range(M):
#         b = [temp[j][i] for j in range(N)]
#         arr_sero.insert(0, ''.join(b))
#     for k in range(N):
#         if arr_garo[k] == ''.join(reversed(arr_garo[k])):
#             return arr_garo[k]
#
#         elif arr_sero[k] == ''.join(reversed(arr_sero[k])):
#             return arr_sero[k]
#
#         else:
#             continue
#
#
# def nm_diff(N, M, temp):
#     arr_garo = list()
#     arr_sero = list()
#     for l in range(20):
#         for i in range(8):
#             arr_garo.append(''.join(temp[l][i:M + i]))
#
#     for k in range(160):
#         if arr_garo[k] == reversed(arr_garo[k]):
#             return arr_garo[k]
#
#
#
# T=int(input())
# a = list()
# i = 0
# result = list()
# for t in range(T):  # T
#     N, M = map(int, input().split())
#     temp = list()
#
#     for l in range(M):
#         temp.append(list(input()))
#
#     if N == M:
#         result.append(nm_equal(N, M, temp))
#
#     else:
#         result.append(nm_diff(N, M, temp))
#
# print(temp)
# for i,value in enumerate(result):
#     print('#{} {}'.format(i+1,value))

